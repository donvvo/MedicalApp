from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from ...utils import *
from MedicalAppointments.models import Patient


@python_2_unicode_compatible
class TreatmentPlan(models.Model):
    patient = models.ForeignKey(Patient)
    date_added = models.DateTimeField(auto_now_add=True)
    plan_name = MyCharField(max_length=50)
    approved = MyCharField(max_length=50)

    def __str__(self):
        return "Treatment plan for " + str(self.patient)


@python_2_unicode_compatible
class DateSignature(models.Model):
    patient = models.ForeignKey(Patient)
    signature_date = MyDateTimeField()
    signature = MyCharField(max_length=50)

    def __str__(self):
        return "Date and signature for " + str(self.patient)
