import logging

from django import forms

from .models import *
from .patient_consent_forms import *
from .patient_forms import *
from .doctor_forms import *

logger = logging.getLogger(__name__)


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