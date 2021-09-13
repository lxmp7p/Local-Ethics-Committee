from pyexpat import model

from django import forms

from .models import Files
from .models import Researh


class Research(forms.ModelForm):
    class Meta:
        model = Researh
        fields = ('type_request', 'identityCode', 'version', 'owner', 'type')


class ClinicalResearchInformationForm(forms.ModelForm):
    """Форма клинического исследования"""
    class Meta:
        model = Researh
        fields = (
            'type_request', 'identityCode', 'version', 'owner', 'type',
            "protocol_name", "drug_name", "main_researcher", "research_center",
            "customer", "customer_contacts", "duration",  "protocol_number", 
        )


class PreclinicalResearchInformationForm(forms.ModelForm):
    """Форма клинического исследования"""
    class Meta:
        model = Researh
        fields = (
            'type_request', 'identityCode', 'version', 'owner', 'type',
            "work_name", "division", "executor",
        )


class ResearchMainDataForm(forms.ModelForm):
    """Форма клинического исследования"""
    class Meta:
        model = Researh
        fields = (
            'type_request', 'identityCode', 'version', 'owner', 'type',
            "type", "type_request", "owner", "identityCode",
            "date_accepted", "version",
        )