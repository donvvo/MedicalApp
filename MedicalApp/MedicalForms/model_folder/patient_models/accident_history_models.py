from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from ...utils import *
from MedicalAppointments.models import Patient


# Accident history choices
ROAD_CONDITION_CHOICES = (
    ('Dry', 'Dry'),
    ('Wet/Rainy', 'Wet/Rainy'),
    ('Snow', 'Snow')
)
COLLISION_TYPE_CHOICES = (
    ('Front-End', 'Front-End'),
    ('Side-End', 'Side-End'),
    ('Side-Swipe', 'Side-Swipe'),
    ('Rear-End', 'Rear-End')
)
EXIT_FROM_VEHICLE_CHOICES = (
    ('Self-powered', 'Self-powered'),
    ('Required Assistance', 'Required Assistance')
)
DOMINANT_HAND_CHOICES = (
    ('Left', 'Left'),
    ('Right', 'Right')
)
IMMEDIATE_LATER_CHOICES = (
    ('Immediate', 'Immediate'),
    ('Later', 'Later')
)
TRANSPORTATION_CHOICES = (
    ('By ambulance', 'By ambulance'),
    ('Own transportation', 'Own transportation')
)


@python_2_unicode_compatible
class PassengerLocation(models.Model):
    choice = models.CharField(max_length=20)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class BodyPart(models.Model):
    choice = models.CharField(max_length=20)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class ShouldersLeftRight(models.Model):
    choice = models.CharField(max_length=20)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class LegsLeftRight(models.Model):
    choice = models.CharField(max_length=20)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class ArmsLeftRight(models.Model):
    choice = models.CharField(max_length=20)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class EmergencyPersonnel(models.Model):
    choice = models.CharField(max_length=20)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class Examinations(models.Model):
    choice = models.CharField(max_length=20)

    def __str__(self):
        return self.choice


# Accident history
@python_2_unicode_compatible
class AccidentHistory(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    today_date = models.DateTimeField(auto_now_add=True)
    description_and_location = MyTextField()
    road_condition = MySelectField(max_length=10,
                                      choices=ROAD_CONDITION_CHOICES)
    anticipation_of_accident = MyNullBooleanField()
    time_of_the_day = MyDateTimeField()
    patient_vehicle = MyCharField(max_length=30)
    patient_vehicle_speed = MyIntegerField()
    other_vehicle = MyCharField(max_length=30)
    other_vehicle_speed = MyIntegerField()
    collision_type = MySelectField(max_length=30,
                                      choices=COLLISION_TYPE_CHOICES)
    vehicle_towed = MyNullBooleanField()
    impact_with_objects = MyNullBooleanField()
    impact_with_objects_detail = MyCharField(max_length=50)
    exit_from_vehicle = MySelectField(max_length=30,
                                         choices=EXIT_FROM_VEHICLE_CHOICES)
    loss_of_consciousness = MyNullBooleanField()
    safety_equipment = MyNullBooleanField()
    airbag_deployed = MyNullBooleanField()
    driver = MyNullBooleanField()
    passengers = models.ManyToManyField(PassengerLocation, blank=True)
    dominant_hand = MySelectField(max_length=20,
                                     choices=DOMINANT_HAND_CHOICES)
    body_part_collision = models.ManyToManyField(BodyPart, blank=True)

    # Symptoms following accident
    headache = MySelectField(max_length=10, choices=IMMEDIATE_LATER_CHOICES)
    dizziness = MySelectField(max_length=10, choices=IMMEDIATE_LATER_CHOICES)
    chest_pain = MySelectField(max_length=10, choices=IMMEDIATE_LATER_CHOICES)
    nausea_voimit = MySelectField(max_length=10, choices=IMMEDIATE_LATER_CHOICES)
    bleeding = MyCharField(max_length=30)
    head_neck = MySelectField(max_length=10, choices=IMMEDIATE_LATER_CHOICES)
    back = MySelectField(max_length=10, choices=IMMEDIATE_LATER_CHOICES)
    shoulders = MySelectField(max_length=10, choices=IMMEDIATE_LATER_CHOICES)
    shoulders_which = models.ManyToManyField(ShouldersLeftRight, blank=True)
    legs = MySelectField(max_length=10, choices=IMMEDIATE_LATER_CHOICES)
    legs_which = models.ManyToManyField(LegsLeftRight, blank=True)
    arms = MySelectField(max_length=10, choices=IMMEDIATE_LATER_CHOICES)
    arms_which = models.ManyToManyField(ArmsLeftRight, blank=True)
    other = MyCharField(max_length=50)
    emergency_personnel = models.ManyToManyField(EmergencyPersonnel, blank=True)
    hospitalized = MyNullBooleanField()
    hospitalized_detail = MyCharField(max_length=100)
    transportation = MySelectField(max_length=20, choices=TRANSPORTATION_CHOICES)
    examination_date = MyDateTimeField()
    examination_type = models.ManyToManyField(Examinations, blank=True)
    examination_other = MyCharField(max_length=20)
    treatment = MyCharField(max_length=50)
    seen_doctor = MyNullBooleanField()
    doctor_name = MyCharField(max_length=50)
    doctor_date = MyDateTimeField()
    treatment_recommendation = MyCharField(max_length=100)

    def __str__(self):
        return 'Accident History for ' + str(self.patient)