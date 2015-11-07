from django.contrib import admin

# Register your models here.
from .models import Clinic, Patient


@admin.register(Clinic, Patient)
class ClinicAdmin(admin.ModelAdmin):
    pass
