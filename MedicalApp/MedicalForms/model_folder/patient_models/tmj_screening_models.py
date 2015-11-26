from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from ...utils import *
from MedicalAppointments.models import Patient


@python_2_unicode_compatible
class Pain(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class Symptom(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class TMJScreening(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    today_date = MyDateTimeField(auto_now_add=True)
    doi = MyDateTimeField()
    pain = models.ManyToManyField(Pain)
    symptom = models.ManyToManyField(Symptom)
    signature = MyCharField(max_length=50)

    def __str__(self):
        return 'TMJ Screening for ' + str(self.patient)