from pyexpat import model

from django import forms

from .models import Information
from .models import Files
from .models import Researh


class ClinicalResearchInformationForm(forms.ModelForm):
    """Форма клинического исследования"""
    class Meta:
        model = Information
        fields = (
            "protocol_name", "drug_name", "main_researcher", "research_center",
            "customer", "customer_contacts", "duration", "research", "protocol_number", "research"
        )


class PreclinicalResearchInformationForm(forms.ModelForm):
    """Форма клинического исследования"""
    class Meta:
        model = Information
        fields = (
            "work_name", "division", "executor", 'research'
        )


class ResearchMainDataForm(forms.ModelForm):
    """Форма клинического исследования"""
    class Meta:
        model = Researh
        fields = (
            "type", "type_request", "owner", "identityCode",
            "date_accepted", "version",
        )