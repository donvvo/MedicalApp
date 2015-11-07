from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from MedicalApp.users.models import User


# Create your models here.
@python_2_unicode_compatible
class Clinic(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class DoctorSpecialty(models.Model):
    specialty = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.specialty


@python_2_unicode_compatible
class Doctor(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    specialty = models.ForeignKey(DoctorSpecialty)
    clinic = models.ForeignKey(Clinic)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


@python_2_unicode_compatible
class Patient(models.Model):
    user = models.OneToOneField(User, primary_key=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Booking(models.Model):
    clinic = models.ForeignKey(Clinic)
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    time = models.DateTimeField()
