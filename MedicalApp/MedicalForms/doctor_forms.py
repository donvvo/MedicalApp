from django import forms

from .models import *


class PlanOfManagementForm(forms.ModelForm):
    class Meta:
        model = PlanOfManagement
        exclude = ('patient', 'today_date')


class PatientDischargeForm(forms.ModelForm):
    class Meta:
        model = PatientDischarge
        exclude = ('patient', 'today_date')
        widgets = {
            'discharge_reason': forms.CheckboxSelectMultiple()
        }


class ReportOfFindingsForm(forms.ModelForm):
    class Meta:
        model = ReportOfFindings
        exclude = ('patient', 'doctor')

