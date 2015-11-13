from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from .utils import *
from MedicalAppointments.models import Patient


SUBJECTIVE_CHOICES = (
    ('Reg.', 'Reg.'),
    ('Irreg.', 'Irreg.'),
    ('Pain/Cramps', 'Pain/Cramps')
)


# Assessment questions
@python_2_unicode_compatible
class Assessment(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    today_date = MyDateTimeField(auto_now_add=True)
    date = MyDateTimeField()
    visit_number = MyIntegerField()
    clinician = MyCharField(max_length=100)
    subjective_choices = MySelectField(max_length=15, choices=SUBJECTIVE_CHOICES)
    subjective_description = MyTextField()
    assessment = MyTextField()
    objective = MyTextField()
    smt = MyTextField()
    stt = MyTextField()
    cardio = MyCharField(max_length=100)
    stretch = MyCharField(max_length=100)
    strength = MyCharField(max_length=100)
    ifc = MyCharField(max_length=100)
    u_s = MyCharField(max_length=100)
    heat = MyCharField(max_length=100)
    ice = MyCharField(max_length=100)
    ohter = MyTextField()
    education = MyTextField()

    def __str__(self):
        return 'Assessment for ' + str(self.patient)
