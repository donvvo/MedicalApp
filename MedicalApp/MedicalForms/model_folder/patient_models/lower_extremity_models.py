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


class LowerExtremityManager(models.Manager):
    def table_summary(self):
        question_list = [
            'question_1',
            'question_2',
            'question_3',
            'question_4',
            'question_5',
            'question_6',
            'question_7',
            'question_8',
            'question_9',
            'question_10',
            'question_11',
            'question_12',
            'question_13',
            'question_14',
            'question_15',
            'question_16',
            'question_17',
            'question_18',
            'question_19',
            'question_20'
        ]

        summary = {}
        choices = ['0', '1', '2', '3', '4']
        for question in question_list:
            row_summary = []
            for choice in choices:
                query = {question: choice}
                row_summary.append(super(LowerExtremityManager, self).get_queryset().filter(**query).count())
            summary[question] = row_summary

        return summary


@python_2_unicode_compatible
class LowerExtremity(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    last_modified = models.DateTimeField(auto_now=True)

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

    objects = LowerExtremityManager()

    def __str__(self):
        return 'Lower Extremity Functional Scale (LEFS) for ' + str(self.patient)