from django import forms

from .models import *


class PatientInformationForm(forms.ModelForm):
    class Meta:
        model = PatientInformation
        exclude = ('patient', 'today_date')


class HealthHistoryForm(forms.ModelForm):
    class Meta:
        model = HealthHistory
        exclude = ('patient', 'today_date')
        widgets = {
            'general': forms.CheckboxSelectMultiple(),
            'muscle_joint': forms.CheckboxSelectMultiple(),
            'skin': forms.CheckboxSelectMultiple(),
            'respiratory': forms.CheckboxSelectMultiple(),
            'gastrointestinal': forms.CheckboxSelectMultiple(),
            'genitourinary': forms.CheckboxSelectMultiple(),
            'cardiovascular': forms.CheckboxSelectMultiple(),
            'women_only_choices': forms.CheckboxSelectMultiple(),
            'previous_conditions': forms.CheckboxSelectMultiple()
        }


class AccidentHistoryForm(forms.ModelForm):
    class Meta:
        model = AccidentHistory
        exclude = ('patient', 'today_date')
        widgets = {
            'passengers': forms.CheckboxSelectMultiple(),
            'body_part_collision': forms.CheckboxSelectMultiple(),
            'shoulders_which': forms.CheckboxSelectMultiple(),
            'legs_which': forms.CheckboxSelectMultiple(),
            'arms_which': forms.CheckboxSelectMultiple(),
            'emergency_personnel': forms.CheckboxSelectMultiple(),
            'examination_type': forms.CheckboxSelectMultiple(),
            'collision_type': forms.RadioSelect(
                                choices=COLLISION_TYPE_CHOICES,
                                attrs={
                                    'type': 'radio'
                                })
        }


class TMJScreeningForm(forms.ModelForm):
    class Meta:
        model = TMJScreening
        exclude = ('patient', )
        widgets = {
            'pain': forms.CheckboxSelectMultiple(),
            'symptom': forms.CheckboxSelectMultiple()
        }


class LowerExtremityForm(forms.ModelForm):
    class Meta:
        model = LowerExtremity
        exclude = ('patient', )


class UpperExtremityForm(forms.ModelForm):
    class Meta:
        model = UpperExtremity
        exclude = ('patient', )

