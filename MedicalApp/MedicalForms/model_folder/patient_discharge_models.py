from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from ..utils import *
from MedicalAppointments.models import Patient


MARITAL_STATUS_CHOICES = (
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Divorced', 'Divorced'),
    ('Common Law', 'Common Law')
)


@python_2_unicode_compatible
class DischargeReasons(models.Model):
    choice = models.CharField(max_length=200)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class PatientDischarge(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    today_date = models.DateTimeField(auto_now_add=True)
    discharge_reason = models.ManyToManyField(DischargeReasons, blank=True)
    initial_complaint = MyTextField()
    progress_to_date = MyTextField()
    reccurance_recommendation = MyTextField()
    risks_complications = MyTextField()
    schedule_date = MyDateTimeField()
    communication = MyCharField(max_length=100)
    other_notes = MyTextField()
    clinician = MyCharField(max_length=100)
    sign_date = MyDateTimeField()

    def __str__(self):
        return 'Patient Discharge for ' + str(self.patient)