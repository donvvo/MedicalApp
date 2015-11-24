from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from ...utils import *
from MedicalAppointments.models import Patient


SCALE_CHOICES = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)


@python_2_unicode_compatible
class NeckDisability(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)

    question_1 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_2 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_3 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_4 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_5 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_6 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_7 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_8 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_9 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_10 = MyRadioField(max_length=2, choices=SCALE_CHOICES)

    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Neck Disability Index for ' + str(self.patient)