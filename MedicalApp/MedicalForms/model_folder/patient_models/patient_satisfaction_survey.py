from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from ...utils import *
from MedicalAppointments.models import Patient


PATIENT_TYPE_CHOICES = (
    ('Private', 'Private'),
    ('WSIB', 'WSIB'),
    ('MVA', 'MVA'),
    ('Other', 'Other')
)

CHOICES = (
    ('a', 'a'),
    ('b', 'b'),
    ('c', 'c'),
    ('d', 'd'),
    ('e', 'e'),
    ('f', 'f')
)


@python_2_unicode_compatible
class PatientSatisfactionSurvey(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    last_modified = models.DateTimeField(auto_now=True)
    submitted = HiddenBooleanField(default=False)

    patient_type = MyRadioField(max_length=10, choices=PATIENT_TYPE_CHOICES)
    patient_type_other = MyCharField(max_length=30)

    question_1 = MyRadioField(max_length=2, choices=CHOICES)
    question_2 = MyRadioField(max_length=2, choices=CHOICES)
    question_3 = MyRadioField(max_length=2, choices=CHOICES)
    question_4 = MyRadioField(max_length=2, choices=CHOICES)
    question_5 = MyRadioField(max_length=2, choices=CHOICES)
    question_6 = MyRadioField(max_length=2, choices=CHOICES)
    question_7 = MyRadioField(max_length=2, choices=CHOICES)

    comments = MyTextField()

    def __str__(self):
        return 'Patient satisfaction survey for ' + str(self.patient)
