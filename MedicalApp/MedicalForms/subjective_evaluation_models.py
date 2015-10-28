from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator, MinValueValidator

from MedicalApp.users.models import User


# Subjective evaluation question choices
@python_2_unicode_compatible
class PresentPain(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class TypeOfPainOthers(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class TypeOfPainHeadache(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class AggravatedByOthers(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class AggravatedByHeadache(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class AggravatedByPeripheralJoint(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class OtherConditions(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


# Subjective evaluation questions
class BaseQuestions(models.Model):
    user = models.ForeignKey(User)
    today_date = models.DateTimeField(auto_now_add=True, blank=True)
    present_pain = models.ManyToManyField(PresentPain, blank=True)
    intensity = models.IntegerField(blank=True,
                                    validators=[
                                        MaxValueValidator(10),
                                        MinValueValidator(0)
                                    ])
    duration = models.CharField(max_length=20, blank=True)
    numbness = models.NullBooleanField()
    paraesthesia = models.NullBooleanField()
    aggravated_by_movements = models.CharField(max_length=100)
    relieved_by = models.NullBooleanField()

    class Meta:
        abstract = True


@python_2_unicode_compatible
class HeadacheQuestions(BaseQuestions):
    type_of_pain = models.ManyToManyField(TypeOfPainHeadache, blank=True)
    aggravated_by = models.ManyToManyField(AggravatedByHeadache, blank=True)

    def __str__(self):
        return 'Headache questions for ' + self.user.first_name
        + ' ' + self.user.last_name


class OtherQuestions(BaseQuestions):
    type_of_pain = models.ManyToManyField(TypeOfPainOthers, blank=True)
    radiation = models.NullBooleanField()
    pain_location = models.CharField(max_length=100)
    aggravated_by = models.ManyToManyField(AggravatedByOthers, blank=True)


@python_2_unicode_compatible
class CervicalSpineQuestions(OtherQuestions):
    def __str__(self):
        return 'Cervical spine questions for ' + self.user.first_name
        + ' ' + self.user.last_name


@python_2_unicode_compatible
class ThoracicSpineQuestions(BaseQuestions):
    def __str__(self):
        return 'Thoracic spine questions for ' + self.user.first_name
        + ' ' + self.user.last_name


@python_2_unicode_compatible
class LumbarSpineQuestions(BaseQuestions):
    def __str__(self):
        return 'Lumbar spine questions for ' + self.user.first_name
        + ' ' + self.user.last_name


class PeripheralJointBaseQuestions(BaseQuestions):
    type_of_pain = models.ManyToManyField(TypeOfPainOthers, blank=True)
    radiation = models.NullBooleanField()
    pain_location = models.CharField(max_length=100)
    aggravated_by = models.ManyToManyField(AggravatedByPeripheralJoint,
                                           blank=True)


@python_2_unicode_compatible
class PeripheralJointQuestions1(PeripheralJointBaseQuestions):
    def __str__(self):
        return 'Peripheral joint 1 questions for ' + self.user.first_name
        + ' ' + self.user.last_name


@python_2_unicode_compatible
class PeripheralJointQuestions2(PeripheralJointBaseQuestions):
    def __str__(self):
        return 'Peripheral joint 2 questions for ' + self.user.first_name
        + ' ' + self.user.last_name


@python_2_unicode_compatible
class PeripheralJointQuestions3(PeripheralJointBaseQuestions):
    def __str__(self):
        return 'Peripheral joint 3 questions for ' + self.user.first_name
        + ' ' + self.user.last_name


@python_2_unicode_compatible
class PeripheralJointQuestions4(PeripheralJointBaseQuestions):
    def __str__(self):
        return 'Peripheral joint 4 questions for ' + self.user.first_name
        + ' ' + self.user.last_name


@python_2_unicode_compatible
class OtherSubjectiveEvaluationQuestions(models.Model):
    users = models.ForeignKey(User)
    today_date = models.DateTimeField(auto_now_add=True, blank=True)
    conditions = models.ManyToManyField(OtherConditions, blank=True)

    def __str__(self):
        return 'Other subjective evaluation questions for ' + self.user.first_name
        + ' ' + self.user.last_name







