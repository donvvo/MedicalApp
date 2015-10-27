from django.contrib import admin
# Register your models here.
from .models import General, MuscleJoint, HealthHistory


@admin.register(General, MuscleJoint, HealthHistory)
class HealthHistoryAdmin(admin.ModelAdmin):
    pass

