import logging

from django import forms

from .models import *

logger = logging.getLogger(__name__)


class ChiropracticTreatmentForm(forms.ModelForm):
    class Meta:
        model = ChiropracticTreatment
        exclude = ('patient', 'last_modified')


class PhysiotherapyTreatmentForm(forms.ModelForm):
    class Meta:
        model = PhysiotherapyTreatment
        exclude = ('patient', 'last_modified')


class MassageTreatmentForm(forms.ModelForm):
    class Meta:
        model = MassageTreatment
        exclude = ('patient', 'last_modified')


class MedicalAuthorizationForm(forms.ModelForm):
    class Meta:
        model = MedicalAuthorization
        exclude = ('patient', 'last_modified')


class ExchangeInformationForm(forms.ModelForm):
    class Meta:
        model = ExchangeInformation
        exclude = ('patient', 'last_modified')


class AuthorizationAndDirectionForm(forms.ModelForm):
    class Meta:
        model = AuthorizationAndDirection
        exclude = ('patient', 'last_modified')


class Section47Form(forms.ModelForm):
    class Meta:
        model = Section47
        exclude = ('patient', 'last_modified')


class StatutoryAccidentsBenefitsForm(forms.ModelForm):
    class Meta:
        model = StatutoryAccidentsBenefits
        exclude = ('patient', 'last_modified')
