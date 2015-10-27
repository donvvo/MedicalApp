import logging

from django import forms

from .models import PatientInformation, HealthHistory, HeadacheQuestions,\
    CervicalSpineQuestions, ThoracicSpineQuestions, LumbarSpineQuestions,\
    PeripheralJointQuestions1, PeripheralJointQuestions2,\
    PeripheralJointQuestions3, PeripheralJointQuestions4,\
    OtherSubjectiveEvaluationQuestions

logger = logging.getLogger(__name__)


class PatientInformationForm(forms.ModelForm):
    class Meta:
        model = PatientInformation
        exclude = ('user', 'today_date')


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








