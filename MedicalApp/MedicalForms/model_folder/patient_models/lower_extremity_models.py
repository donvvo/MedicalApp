from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from ...utils import *
from MedicalAppointments.models import Patient


SCALE_CHOICES = (
    ('0', 'Extreme difficulty or unable to perform activity'),
    ('1', 'Quite a bit of difficulty'),
    ('2', 'Moderate difficulty'),
    ('3', 'A little bit of difficulty'),
    ('4', 'No difficulty')
)


@python_2_unicode_compatible
class LowerExtremity(models.Model):
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
    question_11 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_12 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_13 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_14 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_15 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_16 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_17 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_18 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_19 = MyRadioField(max_length=2, choices=SCALE_CHOICES)
    question_20 = MyRadioField(max_length=2, choices=SCALE_CHOICES)

    def __str__(self):
        return 'Lower Extremity Functional Scale (LEFS) for ' + str(self.patient)