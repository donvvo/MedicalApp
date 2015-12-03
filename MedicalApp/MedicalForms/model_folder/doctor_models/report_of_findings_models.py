from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from MedicalAppointments.models import Doctor, Patient
from ...utils import *


@python_2_unicode_compatible
class ReportOfFindings(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    last_modified = models.DateTimeField(auto_now=True)
    date_of_assessment = MyDateField()
    presenting_complaint = MyTextField()
    examination_findings = MyTextField()
    diagnosis = MyTextField()
    plan_of_management = MyTextField()
    goals = MyTextField()
    risks_discussed = MyTextField()
    alternatives = MyTextField()
    prognosis = MyTextField()
    estimated_time_for_recovery = MyCharField(max_length=20)
    patient_questions = MyTextField()
    signature_date = MyDateField()
    patient_signature = MyCharField(max_length=50)
    clinician_signature = MyCharField(max_length=50)

    def __str__(self):
        return 'Report of Findings for ' + str(self.patient)
