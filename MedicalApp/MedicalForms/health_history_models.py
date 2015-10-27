from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from MedicalApp.users.models import User


MENSTRUAL_FLOW_CHOICES = (
    ('Reg.', 'Reg.'),
    ('Irreg.', 'Irreg.'),
    ('Pain/Cramps', 'Pain/Cramps')
)


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


@python_2_unicode_compatible
class WomenOnlyChoices(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class PreviousConditions(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


# Health history
@python_2_unicode_compatible
class HealthHistory(models.Model):
    user = models.OneToOneField(User)
    today_date = models.DateTimeField(auto_now_add=True, blank=True)
    general = models.ManyToManyField(General, blank=True)
    muscle_joint = models.ManyToManyField(MuscleJoint, blank=True)
    skin = models.ManyToManyField(Skin, blank=True)
    respiratory = models.ManyToManyField(Respiratory, blank=True)
    gastrointestinal = models.ManyToManyField(Gastrointestinal, blank=True)
    genitourinary = models.ManyToManyField(Genitourinary, blank=True)
    cardiovascular = models.ManyToManyField(Cardiovascular, blank=True)
    woemn_only_choices = models.ManyToManyField(WomenOnlyChoices)
    menstrual_flow = models.CharField(max_length=20,
                                      choices=MENSTRUAL_FLOW_CHOICES,
                                      blank=True)
    pregnant = models.NullBooleanField()
    previous_conditions = models.ManyToManyField(PreviousConditions,
                                                 blank=True)
    cnd_disorders = models.CharField(max_length=100, blank=True)
    current_medications = models.TextField(blank=True)
    previous_surgeries = models.TextField(blank=True)
    smoker = models.NullBooleanField(blank=True)
    other_conditions = models.TextField(blank=True)
    family_doctor = models.CharField(max_length=100, blank=True)
    family_doctor_telephone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return 'Health history for ' + self.user.first_name
        + ' ' + self.user.last_name