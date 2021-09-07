import folder as folder
from django.core.files.storage import FileSystemStorage

from ..forms import ClinicalResearchInformationForm
from ..models import Researh, Files
import datetime
import re

now = datetime.datetime.now()

def AddResearch(request=None, researchType=None, requestType=None):
    """Добавление исследования"""
    if requestType == "firstRequest":
        researchId = addResearchMainData(request, researchType, requestType)
        if researchType == "clinicalResearch":
            protocol_number = AddClinicalResearch(request, researchId)
    saveFiles(request.FILES, request.POST, protocol_number, researchId)


def addResearchMainData(request, researchType, requestType):
    """Добавление служеюных данных исследования"""
    Researh.objects.create(type_request=requestType, identityCode='rand', version='1', owner='lxmp7p', type=researchType)
    research = Researh.objects.all().last()
    return research.id


def AddClinicalResearch(request, idResearch):
    """Добавление клинического исследования"""
    protocol_number = None
    informationForm = ClinicalResearchInformationForm(request.POST)
    if informationForm.is_valid():
        informationForm = informationForm.save(commit=False)
        protocol_number = informationForm.protocol_number
        informationForm.info_research_id = idResearch
        informationForm.save()
    return protocol_number

def getFileInfo(filesInfo, file):
    date, version, name = '', '', ''
    if filesInfo.get(file+'_date'):
        date = filesInfo.get(file+'_date')
    if filesInfo.get(file+'_version'):
        version = filesInfo.get(file+'_version')
    if filesInfo.get(file+'_name'):
        name = filesInfo.get(file+'name')
    return date, version, name

def saveFiles(files, filesInfo, protocol_number, researchId):
    """Сохранение файлов и запись в БД информации о них"""
    folder_name = f'/{str(now.strftime("%Y"))}/{protocol_number}/'
    fs = FileSystemStorage()
    fs.base_location = fs.base_location + folder_name
    for file in files:
        fileList = files.getlist(file)
        for myFile in fileList:
            # Удаляем нежелательные символы в имена файла
            filename = re.sub('[!@#$*]', '', myFile.name)
            # Сохранение файла на сервере
            fs.save(filename, myFile)
            # Запись данных в БД
            fileUrl = folder_name[1:] + filename
            date, version, name = getFileInfo(filesInfo, file)
            Files.objects.create(
                file=fileUrl, research_id=researchId,
                date=date, version=version, name=name
            )


