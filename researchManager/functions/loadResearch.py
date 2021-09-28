from django.contrib.contenttypes.models import ContentType
from django.core.files.storage import FileSystemStorage

from ..forms import ClinicalResearchInformationForm, PreclinicalResearchInformationForm
from ..models import Research, Files
import datetime
import re
from collections import defaultdict
import string
import random
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE # these are action flags from the docs

now = datetime.datetime.now()

def AddResearch(request=None, researchType=None, requestType=None, relationshipStatus=None):
    parentResearch = None
    dateAccepted = None
    if request.POST.get("date_accepted"):
        dateAccepted = request.POST.get("date_accepted")
    if relationshipStatus == "true":
        parentResearch = Research.objects.filter(id=request.POST.get("relationResearchId")).order_by('-date_accepted').last()
        identityCode = parentResearch.identityCode
    else:
        identityCode = createIdentityCode()
    folderName, researchId = CreateResearch(request, researchType, requestType, identityCode, dateAccepted)
    folderName = getValidPath(folderName)
    saveFiles(request.FILES, request.POST, folderName, researchId, parentResearch)

def get_typeResearch(typeEng):
    if typeEng == 'clinicalResearch':
        return "Клиническое исследование"
    if typeEng == 'preclinicalResearch':
        return "Доклиническое исследование"
    if typeEng == 'initiativeResearch':
        return "Инициативное исследование"
    if typeEng == 'dissertationWork':
        return "Диссертационная работа"
    raise ValueError('Undefined type Research: {}'.format(str))

def get_typeResearch(typeEng):
    if typeEng == 'clinicalResearch':
        return "Клиническое исследование"
    if typeEng == 'preclinicalResearch':
        return "Доклиническое исследование"
    if typeEng == 'initiativeResearch':
        return "Инициативное исследование"
    if typeEng == 'dissertationWork':
        return "Диссертационная работа"
    raise ValueError('Undefined type Research: {}'.format(str))

def CreateResearch(request, researchType, requestType, identityCode, dateAccepted):
    """
    Добавление клинического исследования
    * Оптимизировать и уменьшить IF
    """
    checkidentityCode = False
    folderName = None
    if researchType == "clinicalResearch":
        informationForm = ClinicalResearchInformationForm(request.POST)
    if researchType == "preclinicalResearch":
        informationForm = PreclinicalResearchInformationForm(request.POST)
    if researchType == "initiativeResearch":
        informationForm = InitiativeResearchInformationForm(request.POST)
    if researchType == "dissertationWork":
        informationForm = DissertationWorkInformationForm(request.POST)
    if informationForm.is_valid():
        informationForm = informationForm.save(commit=False)
        if researchType == "clinicalResearch":
            folderName = informationForm.protocol_number
        if researchType == "preclinicalResearch":
            folderName = informationForm.work_name
        if researchType == "initiativeResearch":
            folderName = informationForm.name_research
        if researchType == "dissertationWork":
            folderName = informationForm.work_name
        informationForm.type_request=requestType 
        informationForm.identityCode=identityCode
        informationForm.owner=request.user
        informationForm.type=researchType
        informationForm.date_accepted=dateAccepted
        
        researchList = getMainResearchsList(researchType)
        checkidentityCode = False
        for research in researchList:
            if informationForm.identityCode == research.identityCode:
                checkidentityCode = True
                break
        
        informationForm.save()
    researchId = Research.objects.all().last()
    if not researchId:
        researchId = 1
    else:
        researchId = researchId.id
    researchList = getMainResearchsList(researchType)
    return folderName, researchId


def getFileInfo(filesInfo, file):
    """Выдает информацию и пути к файлу, а так же название документа, версию и его дату"""
    date, version, name = '', '', ''
    if filesInfo.get(file + '_date'):
        date = filesInfo[file + '_date'].pop(0)[0:]
    if filesInfo.get(file + '_version'):
        version = filesInfo[file+'_version'].pop(0)[0:]
    name = getFilename(file)
    if filesInfo.get(file + '_name'):
        name = filesInfo[file + '_name'].pop(0)[0:]
    return date, version, name, filesInfo

def saveFiles(files, filesInfo, folderName, researchId, parentResearch):
    """Сохранение файлов и запись в БД информации о них"""
    folder_name = (f'/{str(now.strftime("%Y"))}/{str(folderName)}/')
    if parentResearch and parentResearch.version:
        folder_name += (f"{parentResearch.version + 1}/")
    fs = FileSystemStorage()
    fs.base_location = fs.base_location + folder_name
    filesInfo = filesInfo.copy()
    myDict = dict(filesInfo.lists())
    if parentResearch:
        for file in Files.objects.filter(research=parentResearch):
            Files.objects.create(
                file=file.file, research_id=researchId,
                date=file.date, version=file.version, name=file.name
            )
    for file in files:
        fileList = files.getlist(file)
        for myFile in fileList:
            # Удаляем нежелательные символы в имена файла
            filename = getValidPath(myFile.name)
            # Сохранение файла на сервере
            fs.save(filename, myFile)
            # Запись данных в БД
            fileUrl = folder_name[1:] + filename
            date, version, name, filesInfo = getFileInfo(myDict, file)
            Files.objects.create(
                file=fileUrl, research_id=researchId,
                date=date, version=version, name=name
            )

def createIdentityCode():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 8
    return ''.join(random.choice(chars) for x in range(size,20))

def getResearchHistory(researchId):
    """Выдает текущее исследование, список файлов и историю"""
    research = Research.objects.get(id=researchId)
    filesList = Files.objects.filter(research=research)
    history = []
    relatedResearchs = Research.objects.filter(identityCode=research.identityCode).order_by('-date_accepted')
    for historyResearch in relatedResearchs:
        historyFiles = Files.objects.filter(research=research)
        history.append({"historyResearch": historyResearch, "historyFiles": historyFiles})
    return research, filesList, history

def getMainResearchsList(researchType):
    """Выдает список самых новых исследований с уникальным identityCode"""
    allResearch = Research.objects.filter(type=researchType).order_by('-date_accepted')
    researchList = []
    for notFiltredResearch in allResearch:
        if researchList:
            have = False
            for research in researchList:
                if notFiltredResearch.identityCode == research.identityCode:
                    have = True
                else:
                    if research.date_accepted or notFiltredResearch.date_accepted == None:
                        research = notFiltredResearch
                        have = False
                    elif notFiltredResearch.date_accepted > research.date_accepted:
                        research = notFiltredResearch
                        have = False
            if not have:
                researchList.append(notFiltredResearch)
                have = False
        else: 
            researchList.append(allResearch[0])
    return researchList

def getValidPath(path):
    return re.sub('[!@#$*/\\\\ ]', '-', path)

def getFilename(filenameEng):
    filenameRu = "Неизвестный файл"
    filenameWordlist = {
        "letter": "Письмо в лэк",
        "member_list": "Список членов команды",
        "permit": "Разрешение МЗ РФ",
        "inform_list": "Информационный листок пациента",
        "brochure_researcher": "Брошюра исследователя",
        "protocol": "Протокол исследования",
    } 
    for key in filenameWordlist:
        if key == filenameEng:
            filenameRu = filenameWordlist.get(key)
    return filenameRu
