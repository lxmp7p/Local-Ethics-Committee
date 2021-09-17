from .models import Research
from django.http import JsonResponse, HttpResponse

def get_research_info(request):
    """Выдача основной информации об исследовании"""
    researhInfo = {
            "protocolNumber": research.protocol_number,
            "protocolName": research.protocol_name,
            "drugName": research.drug_name,
            "mainResearcher": research.main_researcher,
            "researchCenter": research.research_center,
            "customer": research.customer,
            "customerContacts": research.customer_contacts,
            "duration": research.duration,
            "name_research": research.name_research,
            "managers": research.managers,
            "specialization": research.specialization,
            "executor": research.executor,
            "division": research.division,
            "work_name": research.work_name,
    }
    return JsonResponse(researhInfo)