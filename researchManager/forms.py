from pyexpat import model

from django import forms

from .models import Files
from .models import Research


class ClinicalResearchInformationForm(forms.ModelForm):
    """Форма клинического исследования"""
    class Meta:
        model = Research
        fields = (
            'type_request', 'identityCode', 'owner', 'type', 'date_accepted',
            "protocol_name", "drug_name", "main_researcher", "research_center",
            "customer", "customer_contacts", "duration",  "protocol_number", 
        )


class PreclinicalResearchInformationForm(forms.ModelForm):
    """Форма доклинического исследования"""
    class Meta:
        model = Research
        fields = (
            'type_request', 'identityCode', 'owner', 'type', 'date_accepted',
            "work_name", "division", "executor",
        )


class InitiativeResearchInformationForm(forms.ModelForm):
    """Форма инициативного исследования"""
    class Meta:
        model = Research
        fields = (
            'type_request', 'identityCode', 'owner', 'type', 'date_accepted',
            "name_research", "main_researcher", "division",
        )


class DissertationWorkInformationForm(forms.ModelForm):
    """Форма инициативного исследования"""
    class Meta:
        model = Research
        fields = (
            'type_request', 'identityCode', 'owner', 'type', 'date_accepted',
            "name_research", "main_researcher", "division",
        )


class ResearchMainDataForm(forms.ModelForm):
    """Форма клинического исследования"""
    class Meta:
        model = Research
        fields = (
            'type_request', 'identityCode', 'owner', 'type', 
            "type", "type_request", "owner", "identityCode",
            "date_accepted",
        )