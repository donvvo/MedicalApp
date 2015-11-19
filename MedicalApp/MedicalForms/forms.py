import logging

from django import forms

from .models import *
from .patient_consent_forms import *
from .patient_forms import *

logger = logging.getLogger(__name__)


class PatientInformationForm(forms.ModelForm):
    class Meta:
        model = PatientInformation
        exclude = ('user', 'today_date')
        widgets = {
            'accident_date': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Date of Accident'
                }),
            'date_of_birth': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Date of Birth'
                }),
            'modified_duties_availability': forms.NullBooleanSelect(
                attrs={
                    'class': 'form-control'
                })
        }


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


# Subjective evaluation
class BaseSubjectiveEvalForm(forms.ModelForm):
    class Meta:
        exclude = ('user', 'today_date')
        widgets = {
            'present_pain': forms.CheckboxSelectMultiple(),
            'type_of_pain': forms.CheckboxSelectMultiple(),
            'aggravated_by': forms.CheckboxSelectMultiple()
        }


class HeadacheQuestionForm(BaseSubjectiveEvalForm):
    class Meta(BaseSubjectiveEvalForm.Meta):
        model = HeadacheQuestions


class CervicalSpineQuestionForm(BaseSubjectiveEvalForm):
    class Meta(BaseSubjectiveEvalForm.Meta):
        model = CervicalSpineQuestions


class ThoracicSpineQuestionForm(BaseSubjectiveEvalForm):
    class Meta(BaseSubjectiveEvalForm.Meta):
        model = ThoracicSpineQuestions


class LumbarSpineQuestionForm(BaseSubjectiveEvalForm):
    class Meta(BaseSubjectiveEvalForm.Meta):
        model = LumbarSpineQuestions


class PeripheralJointQuestion1Form(BaseSubjectiveEvalForm):
    class Meta(BaseSubjectiveEvalForm.Meta):
        model = PeripheralJointQuestions1


class PeripheralJointQuestion2Form(BaseSubjectiveEvalForm):
    class Meta(BaseSubjectiveEvalForm.Meta):
        model = PeripheralJointQuestions2


class PeripheralJointQuestion3Form(BaseSubjectiveEvalForm):
    class Meta(BaseSubjectiveEvalForm.Meta):
        model = PeripheralJointQuestions3


class PeripheralJointQuestion4Form(BaseSubjectiveEvalForm):
    class Meta(BaseSubjectiveEvalForm.Meta):
        model = PeripheralJointQuestions4


class OtherSubjectiveEvaluationQuestionForm(forms.ModelForm):
    class Meta:
        model = OtherSubjectiveEvaluationQuestions
        exclude = ('user', 'today_date')
        widgets = {
            'conditions': forms.CheckboxSelectMultiple()
        }


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        exclude = ('user', 'today_date')


class MVAIntakeForm(forms.ModelForm):
    class Meta:
        model = MVAIntake
        exclude = ('user', 'today_date')


class ReportOffindingsForm(forms.ModelForm):
    class Meta:
        model = ReportOfFindings
        exclude = ('doctor', )


class TMJScreeningForm(forms.ModelForm):
    class Meta:
        model = TMJScreening
        exclude = ('patient', )
        widgets = {
            'pain': forms.CheckboxSelectMultiple(),
            'symptom': forms.CheckboxSelectMultiple()
        }


class AcuteConcussionEvaluationForm(forms.ModelForm):
    class Meta:
        model = AcuteConcussionEvaluation
        exclude = ('patient', 'doctor', 'completed_date')
        widgets = {
            'location_of_impact': forms.CheckboxSelectMultiple(),
            'early_signs': forms.CheckboxSelectMultiple(),
            'red_flags': forms.CheckboxSelectMultiple(),
            'dignosis': forms.CheckboxSelectMultiple(),
            'refferal': forms.CheckboxSelectMultiple(),
        }