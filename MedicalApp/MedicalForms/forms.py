import logging

from django import forms

from .models import PatientInformation

logger = logging.getLogger(__name__)


class PatientInformationForm(forms.ModelForm):
    class Meta:
        model = PatientInformation
        exclude = ()

