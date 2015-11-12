from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from .utils import MyCharField, MySelectField, MyNullBooleanField, MyTextField
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
    user = models.ForeignKey(User)
    today_date = models.DateTimeField(auto_now_add=True, blank=True)
    general = models.ManyToManyField(General, blank=True)
    muscle_joint = models.ManyToManyField(MuscleJoint, blank=True)
    skin = models.ManyToManyField(Skin, blank=True)
    respiratory = models.ManyToManyField(Respiratory, blank=True)
    gastrointestinal = models.ManyToManyField(Gastrointestinal, blank=True)
    genitourinary = models.ManyToManyField(Genitourinary, blank=True)
    cardiovascular = models.ManyToManyField(Cardiovascular, blank=True)
    woemn_only_choices = models.ManyToManyField(WomenOnlyChoices)
    menstrual_flow = MySelectField(max_length=20,
                                      choices=MENSTRUAL_FLOW_CHOICES)
    pregnant = MyNullBooleanField()
    previous_conditions = models.ManyToManyField(PreviousConditions,
                                                 blank=True)
    cnd_disorders = MyCharField(max_length=100)
    current_medications = MyTextField()
    previous_surgeries = MyTextField()
    smoker = MyNullBooleanField()
    other_conditions = MyTextField()
    family_doctor = MyCharField(max_length=100)
    family_doctor_telephone = MyCharField(max_length=20)

    def __str__(self):
        return 'Health history for ' + self.user.first_name
        + ' ' + self.user.last_name