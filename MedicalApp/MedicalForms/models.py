from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from MedicalApp.users.models import User


# Health history questions.
@python_2_unicode_compatible
class General(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class MuscleJoint(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class Skin(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class Respiratory(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class Gastrointestinal(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class Genitourinary(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class Cardiovascular(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


'''@python_2_unicode_compatible
class WomenOnlyChoices(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class WomenOnly(models.Model):
    choice = models.ManyToManyField(WomenOnlyChoices)
    menstrual_flow =

    def __str__(self):
        return self.choice'''


@python_2_unicode_compatible
class PreviousConditions(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


# Health history
@python_2_unicode_compatible
class HealthHistory(models.Model):
    user = models.OneToOneField(User)
    general = models.ManyToManyField(General)
    muscle_joint = models.ManyToManyField(MuscleJoint)
    skin = models.ManyToManyField(Skin)
    respiratory = models.ManyToManyField(Respiratory)
    gastrointestinal = models.ManyToManyField(Gastrointestinal)
    genitourinary = models.ManyToManyField(Genitourinary)
    cardiovascular = models.ManyToManyField(Cardiovascular)
    PreviousConditions = models.ManyToManyField(PreviousConditions)

    def __str__(self):
        return 'Health history for ' + self.user.first_name
        + ' ' + self.user.last_name

