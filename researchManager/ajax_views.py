from .models import Research
from django.http import JsonResponse, HttpResponse

def get_research_info(request):
    """Проверка доступности логина"""
    print(request.GET)
    research = Research.objects.get(id=request.GET.get('relationResearchId'))
    if research.type == 'clinicalResearch':
        researhInfo = {
            "protocolNumber": research.protocol_number,
            "protocolName": research.protocol_name,
            "drugName": research.drug_name,
            "mainResearcher": research.main_researcher,
            "researchCenter": research.research_center,
            "customer": research.customer,
            "customerContacts": research.customer_contacts,
            "duration": research.duration,
        }
    print(researhInfo)
    return JsonResponse(researhInfo)