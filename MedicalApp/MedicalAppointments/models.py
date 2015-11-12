from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

from MedicalApp.users.models import User
from MedicalForms.utils import MyCharField, MySelectField, IntegerRangeField, MyNullBooleanField, MyTextField

# Create your models here.
@python_2_unicode_compatible
class Clinic(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    description = models.TextField(blank=True)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=200, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    start_time = models.CharField(max_length=10, blank=True)
    end_time = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name

    def url_name(self):
        return self.name.replace(' ', '+')


@python_2_unicode_compatible
class DoctorSpecialty(models.Model):
    specialty = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.specialty


@python_2_unicode_compatible
class Doctor(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    specialty = models.ForeignKey(DoctorSpecialty, blank=True, default="Chiropractor")
    clinic = models.ForeignKey(Clinic, blank=True, default="Test Clinic 1")

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' -- ' + \
        'Specialty: ' + self.specialty.specialty + ', Clinic: ' + self.clinic.name


@python_2_unicode_compatible
class Patient(models.Model):
    user = models.OneToOneField(User, primary_key=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


@python_2_unicode_compatible
class Booking(models.Model):
    clinic = models.ForeignKey(Clinic)
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    time = models.DateTimeField()

    def __str__(self):
        return "Booking at " + self.clinic.pk + " at " + \
        timezone.localtime(self.time).strftime('%H:%M -- %m/%d/%y') + \
        " for " + str(self.patient) + " with " + str(self.doctor)
