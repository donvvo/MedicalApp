from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from .utils import *
from MedicalAppointments.models import Patient


@python_2_unicode_compatible
class ChiropracticTreatment(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    signature = MyCharField(max_length=50)
    date = MyDateTimeField()
    name = MyCharField(max_length=50)

    def __str__(self):
        return 'Chiropractic Treatment Consent for ' + str(self.patient)