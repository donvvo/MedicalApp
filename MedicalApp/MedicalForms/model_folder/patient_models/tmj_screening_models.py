from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from ...utils import *
from MedicalAppointments.models import Patient


PAIN_LEVEL_CHOICES = (
    ('Mild', 'Mild'),
    ('Moderate', 'Moderate'),
    ('Severe', 'Severe')
)

PAIN_DESCRIPTION_CHOICES = (
    ('Burning', 'Burning'),
    ('Dull', 'Dull'),
    ('Numbing', 'Numbing'),
    ('Pressure', 'Pressure'),
    ('Sharp', 'Sharp'),
    ('Tingling', 'Tingling'),
    ('Radiating', 'Radiating')
)

PAIN_INTENSITY_CHOICES = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10')
)


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
    last_modified = models.DateTimeField(auto_now=True)
    doi = MyDateTimeField()
    pain = models.ManyToManyField(Pain, blank=True)
    symptom = models.ManyToManyField(Symptom, blank=True)
    signature = MyCharField(max_length=50)
    pain_level_1 = MySelectField(max_length=20, choices=PAIN_LEVEL_CHOICES)
    pain_level_2 = MySelectField(max_length=20, choices=PAIN_LEVEL_CHOICES)
    pain_level_3 = MySelectField(max_length=20, choices=PAIN_LEVEL_CHOICES)
    pain_level_4 = MySelectField(max_length=20, choices=PAIN_LEVEL_CHOICES)
    pain_description_1 = MySelectField(max_length=20, choices=PAIN_DESCRIPTION_CHOICES)
    pain_description_2 = MySelectField(max_length=20, choices=PAIN_DESCRIPTION_CHOICES)
    pain_description_3 = MySelectField(max_length=20, choices=PAIN_DESCRIPTION_CHOICES)
    pain_description_4 = MySelectField(max_length=20, choices=PAIN_DESCRIPTION_CHOICES)
    pain_intensity = MyRadioField(max_length=2, choices=PAIN_INTENSITY_CHOICES)

    def __str__(self):
        return 'TMJ Screening for ' + str(self.patient)