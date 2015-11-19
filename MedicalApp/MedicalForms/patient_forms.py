from django import forms

from .models import *


class PatientInformationForm(forms.ModelForm):
    class Meta:
        model = PatientInformation
        exclude = ('patient', 'today_date')


class AccidentHistoryForm(forms.ModelForm):
    class Meta:
        model = AccidentHistory
        exclude = ('patient', 'today_date')
        widgets = {
            'passengers': forms.CheckboxSelectMultiple(),
            'body_part_collision': forms.CheckboxSelectMultiple()
        }