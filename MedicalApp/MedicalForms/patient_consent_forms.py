import logging

from django import forms

from .models import *

logger = logging.getLogger(__name__)


class ChiropracticTreatmentForm(forms.ModelForm):
    class Meta:
        model = ChiropracticTreatment
        exclude = ('patient', )


class PhysiotherapyTreatmentForm(forms.ModelForm):
    class Meta:
        model = PhysiotherapyTreatment
        exclude = ('patient', )
