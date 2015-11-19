from django import forms

from .models import *


class PlanOfManagementForm(forms.ModelForm):
    class Meta:
        model = PlanOfManagement
        exclude = ('patient', 'today_date')
