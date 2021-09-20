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

def AddResearch(request=None, researchType=None, requestType=None):
    dateAccepted = 's'
    if requestType == "secondRelationRequest":
        parentResearch = Research.objects.get(id=request.POST.get("relationResearchId"))
        dateAccepted = request.POST.get("date_accepted")
        if request.POST.get("date_accepted") == '':
            dateAccepted = None
        identityCode = parentResearch.identityCode
    else:
        identityCode = createIdentityCode()
        dateAccepted = None
    folderName, researchId = CreateResearch(request, researchType, requestType, identityCode, dateAccepted)
    saveFiles(request.FILES, request.POST, folderName, researchId)

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
        informationForm.owner=request.user.username
        informationForm.type=researchType
        informationForm.date_accepted=dateAccepted
        informationForm.save()
    researchId = Research.objects.all().last()

    researchList = getMainResearchsList(researchType)

    for research in researchList:
        if informationForm.identityCode == research.identityCode:
            LogEntry.objects.log_action(
                user_id=request.user.id,
                content_type_id=ContentType.objects.get_for_model(Research).pk,
                bject_repr=informationForm.protocol_number, 
                object_id=researchId.id,
                change_message=informationForm.type_request + get_typeResearch(researchType) + ' : ' + informationForm.protocol_number, 
                action_flag=CHANGE)
        else:
            LogEntry.objects.log_action(
                user_id=request.user.id,
                content_type_id=ContentType.objects.get_for_model(Research).pk,
                bject_repr=informationForm.protocol_number, 
                object_id=researchId.id,
                change_message='Добавил ' + get_typeResearch(researchType) + ' : ' + informationForm.protocol_number, 
                action_flag=ADDITION)
   
    

    

    return folderName, researchId.id

def AddPreclinicalResearch(request, idResearch):
    """Добавление доклинического исследования"""
    work_name = None
    informationForm = PreclinicalResearchInformationForm(request.POST)
    if informationForm.is_valid():
        informationForm = informationForm.save(commit=False)

        informationForm.info_research_id = idResearch
        informationForm.save()
    return work_name

def getFileInfo(filesInfo, file):
    """Выдает информацию и пути к файлу, а так же название документа, версию и его дату"""
    date, version, name = '', '', ''
    if filesInfo.get(file + '_date'):
        date = filesInfo[file + '_date'].pop(0)[0:]
    if filesInfo.get(file + '_version'):
        version = filesInfo[file+'_version'].pop(0)[0:]
    name = file
    return date, version, name, filesInfo

def saveFiles(files, filesInfo, folderName, researchId):
    """Сохранение файлов и запись в БД информации о них"""
    folder_name = f'/{str(now.strftime("%Y"))}/{folderName}/'
    fs = FileSystemStorage()
    fs.base_location = fs.base_location + folder_name
    filesInfo = filesInfo.copy()
    myDict = dict(filesInfo.lists())
    for file in files:
        fileList = files.getlist(file)
        for myFile in fileList:
            # Удаляем нежелательные символы в имена файла
            filename = re.sub('[!@#$*]', '', myFile.name)
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
                    if notFiltredResearch.date_accepted > research.date_accepted:
                        research = notFiltredResearch
                        have = False
            if not have:
                researchList.append(notFiltredResearch)
                have = False
        else: 
            researchList.append(allResearch[0])
    return researchList