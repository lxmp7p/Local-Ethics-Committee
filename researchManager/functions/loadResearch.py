import folder as folder
from django.core.files.storage import FileSystemStorage

from ..forms import ClinicalResearchInformationForm
from ..models import Researh
from ..models import Files
import datetime

now = datetime.datetime.now()

def AddResearch(request=None, researchType=None, requestType=None):
    if requestType == "firstRequest":
        researchId = addResearchMainData(request, researchType, requestType)
        if researchType == "clinicalResearch":
            protocol_number = AddClinicalResearch(request, researchId)
    saveFiles(request.FILES, protocol_number)


def addResearchMainData(request, researchType, requestType):
    Researh.objects.create(type_request=requestType, identityCode='rand', version='1', owner='lxmp7p', )
    research = Researh.objects.all().last()
    return research.id


def AddClinicalResearch(request, idResearch):
    protocol_number = None
    informationForm = ClinicalResearchInformationForm(request.POST)
    if informationForm.is_valid():
        informationForm = informationForm.save(commit=False)
        protocol_number = informationForm.protocol_number
        informationForm.info_research_id = idResearch
        informationForm.save()
    return protocol_number


def saveFiles(files, protocol_number):
    folder_name = f'/{str(now.strftime("%Y"))}/{protocol_number}/'
    fs = FileSystemStorage()
    fs.base_location = fs.base_location + folder_name
    for file in files:
        fileList = files.getlist(file)
        for myFile in fileList:
            filename = fs.save(myFile.name, myFile)


#def save_research_main_data():
