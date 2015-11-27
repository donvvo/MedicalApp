from django import forms

from .models import *


class PlanOfManagementForm(forms.ModelForm):
    class Meta:
        model = PlanOfManagement
        exclude = ('patient', 'last_modified')


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


class PatientSpecificForm(forms.ModelForm):
    class Meta:
        model = PatientSpecific
        exclude = ('patient', )


class TreatmentPlanAddForm(forms.ModelForm):
    class Meta:
        model = TreatmentPlan
        exclude = ('patient', 'date_added')


class DateSignatureAddForm(forms.ModelForm):
    class Meta:
        model = DateSignature
        exclude = ('patient', )

