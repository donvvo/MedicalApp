from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from MedicalApp.users.models import User
from .utils import MyCharField


@python_2_unicode_compatible
class AttendenceSheet(models.Model):
    pass