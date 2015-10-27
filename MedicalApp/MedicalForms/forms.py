import logging

from django import forms

from .models import PatientInformation, HealthHistory

logger = logging.getLogger(__name__)


class PatientInformationForm(forms.ModelForm):
    class Meta:
        model = PatientInformation
        exclude = ('user', 'today_date')


class HealthHistoryForm(forms.ModelForm):
    class Meta:
        model = HealthHistory
        exclude = ('user', 'today_date')
        widgets = {
            'general': forms.CheckboxSelectMultiple(),
            'muscle_joint': forms.CheckboxSelectMultiple(),
            'skin': forms.CheckboxSelectMultiple(),
            'respiratory': forms.CheckboxSelectMultiple(),
            'gastrointestinal': forms.CheckboxSelectMultiple(),
            'genitourinary': forms.CheckboxSelectMultiple(),
            'cardiovascular': forms.CheckboxSelectMultiple(),
            'woemn_only_choices': forms.CheckboxSelectMultiple(),
            'previous_conditions': forms.CheckboxSelectMultiple()
        }

