import logging

from django import forms

from .models import *
from .patient_consent_forms import *
from .patient_forms import *
from .doctor_forms import *

logger = logging.getLogger(__name__)


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        exclude = ('user', 'today_date')


class MVAIntakeForm(forms.ModelForm):
    class Meta:
        model = MVAIntake
        exclude = ('user', 'today_date')