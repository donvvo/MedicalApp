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


class MassageTreatmentForm(forms.ModelForm):
    class Meta:
        model = MassageTreatment
        exclude = ('patient', )


class MedicalAuthorizationForm(forms.ModelForm):
    class Meta:
        model = MedicalAuthorization
        exclude = ('patient', )


class ExchangeInformationForm(forms.ModelForm):
    class Meta:
        model = ExchangeInformation
        exclude = ('patient', )


class AuthorizationAndDirectionForm(forms.ModelForm):
    class Meta:
        model = AuthorizationAndDirection
        exclude = ('patient', )


class Section47Form(forms.ModelForm):
    class Meta:
        model = Section47
        exclude = ('patient', )


class StatutoryAccidentsBenefitsForm(forms.ModelForm):
    class Meta:
        model = StatutoryAccidentsBenefits
        exclude = ('patient', )
