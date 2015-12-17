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


class NeckDisabilityManager(models.Manager):
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
            'question_10'
        ]

        summary = {}
        choices = ['0', '1', '2', '3', '4', '5']
        for question in question_list:
            row_summary = []
            for choice in choices:
                query = {question: choice}
                row_summary.append(super(NeckDisabilityManager, self).get_queryset().filter(**query).count())
            summary[question] = row_summary

        return summary


@python_2_unicode_compatible
class NeckDisability(models.Model):
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

    last_modified = models.DateTimeField(auto_now=True)

    objects = NeckDisabilityManager()

    def __str__(self):
        return 'Neck Disability Index for ' + str(self.patient)