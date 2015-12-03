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
        exclude = ('patient', 'last_modified')


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


class AcuteConcussionEvaluationForm(forms.ModelForm):
    class Meta:
        model = AcuteConcussionEvaluation
        exclude = ('patient', 'last_modified')
        widgets = {
            'location_of_impact': forms.CheckboxSelectMultiple(),
            'early_signs': forms.CheckboxSelectMultiple(),
            'red_flags': forms.CheckboxSelectMultiple(),
            'diagnosis': forms.CheckboxSelectMultiple(),
            'refferal': forms.CheckboxSelectMultiple(),
        }

# Subjective evaluation
class BaseSubjectiveEvalForm(forms.ModelForm):
    class Meta:
        exclude = ('patient', 'last_modified')
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
        exclude = ('patient', 'last_modified')
        widgets = {
            'conditions': forms.CheckboxSelectMultiple()
        }