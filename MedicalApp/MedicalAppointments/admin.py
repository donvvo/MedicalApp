from django.contrib import admin

# Register your models here.
from .models import Clinic, Patient, DoctorSpecialty, Doctor, Booking


@admin.register(Clinic, Patient, DoctorSpecialty, Doctor, Booking)
class ClinicAdmin(admin.ModelAdmin):
    pass
