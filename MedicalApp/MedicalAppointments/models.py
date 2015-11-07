from django.db import models

from MedicalApp.users.models import User


# Create your models here.
class Clinic(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=10)


class Doctor(models.Model):
    user = models.OneToOneField(User, primary_key=True)


class Patient(models.Model):
    user = models.OneToOneField(User, primary_key=True)
