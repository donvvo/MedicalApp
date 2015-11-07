from django.contrib import admin

# Register your models here.
from .models import Clinic, Patient, DoctorSpecialty, Doctor


@admin.register(Clinic, Patient, DoctorSpecialty, Doctor)
class ClinicAdmin(admin.ModelAdmin):
    pass
