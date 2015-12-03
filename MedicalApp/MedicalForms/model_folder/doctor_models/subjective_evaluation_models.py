from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from ...utils import *
from MedicalAppointments.models import Patient


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
    patient = models.OneToOneField(Patient, primary_key=True)
    last_modified = models.DateTimeField(auto_now=True)
    present_pain = models.ManyToManyField(PresentPain, blank=True)
    intensity = IntegerRangeField(min_value=0, max_value=0)
    duration = MyCharField(max_length=20)
    numbness = MyNullBooleanField()
    paraesthesia = MyNullBooleanField()
    aggravated_by_movements = MyCharField(max_length=100)
    relieved_by = MyNullBooleanField()

    class Meta:
        abstract = True


@python_2_unicode_compatible
class HeadacheQuestions(BaseQuestions):
    type_of_pain = models.ManyToManyField(TypeOfPainHeadache, blank=True)
    aggravated_by = models.ManyToManyField(AggravatedByHeadache, blank=True)

    def __str__(self):
        return 'Headache questions for ' + str(self.patient)


class OtherQuestions(BaseQuestions):
    type_of_pain = models.ManyToManyField(TypeOfPainOthers, blank=True)
    radiation = MyNullBooleanField()
    pain_location = MyCharField(max_length=100)
    aggravated_by = models.ManyToManyField(AggravatedByOthers, blank=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class CervicalSpineQuestions(OtherQuestions):
    def __str__(self):
        return 'Cervical spine questions for ' + str(self.patient)


@python_2_unicode_compatible
class ThoracicSpineQuestions(OtherQuestions):
    def __str__(self):
        return 'Thoracic spine questions for ' + str(self.patient)


@python_2_unicode_compatible
class LumbarSpineQuestions(OtherQuestions):
    def __str__(self):
        return 'Lumbar spine questions for ' + str(self.patient)


class PeripheralJointBaseQuestions(BaseQuestions):
    type_of_pain = models.ManyToManyField(TypeOfPainOthers, blank=True)
    radiation = MyNullBooleanField()
    pain_location = MyCharField(max_length=100)
    aggravated_by = models.ManyToManyField(AggravatedByPeripheralJoint,
                                           blank=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class PeripheralJointQuestions1(PeripheralJointBaseQuestions):
    def __str__(self):
        return 'Peripheral joint 1 questions for ' + str(self.patient)


@python_2_unicode_compatible
class PeripheralJointQuestions2(PeripheralJointBaseQuestions):
    def __str__(self):
        return 'Peripheral joint 2 questions for ' + str(self.patient)


@python_2_unicode_compatible
class PeripheralJointQuestions3(PeripheralJointBaseQuestions):
    def __str__(self):
        return 'Peripheral joint 3 questions for ' + str(self.patient)


@python_2_unicode_compatible
class PeripheralJointQuestions4(PeripheralJointBaseQuestions):
    def __str__(self):
        return 'Peripheral joint 4 questions for ' + str(self.patient)


@python_2_unicode_compatible
class OtherSubjectiveEvaluationQuestions(models.Model):
    patient = models.OneToOneField(Patient)
    last_modified = models.DateTimeField(auto_now=True)
    conditions = models.ManyToManyField(OtherConditions, blank=True)

    def __str__(self):
        return 'Other subjective evaluation questions for ' + str(self.patient)







