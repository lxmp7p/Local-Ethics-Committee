from django.core.files.storage import FileSystemStorage

from ..forms import ClinicalResearchInformationForm, PreclinicalResearchInformationForm
from ..models import Researh, Files, Information
import datetime
import re
from collections import defaultdict


now = datetime.datetime.now()

def AddResearch(request=None, researchType=None, requestType=None):
    """
    - Добавление исследования
    Для добавления нового типа исследования нужно:
    -> AddResearchInformation()
    """
    researchId = addResearchMainData(researchType, requestType)
    if researchId:
        folderName = AddResearchInformation(request, researchId, researchType)
    if folderName:
        saveFiles(request.FILES, request.POST, folderName, researchId)


def addResearchMainData(researchType, requestType):
    """Добавление служебных данных исследования"""
    Researh.objects.create(type_request=requestType, identityCode='rand', version='1', owner='lxmp7p', type=researchType)
    research = Researh.objects.all().last()
    return research.id

def AddResearchInformation(request, idResearch, researchType):
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
        informationForm = PreclinicalResearchInformationForm(request.POST)
    if researchType == "dissertationWork":
        informationForm = PreclinicalResearchInformationForm(request.POST)
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
        informationForm.research_id = idResearch
        informationForm.save()
    return folderName

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
    if filesInfo.get(file + '_name'):
        name = filesInfo.pop(0)[0:]
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