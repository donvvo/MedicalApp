from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from MedicalApp.users.models import User

from .patient_info_models import *
from .health_history_models import *


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


# Accident history
@python_2_unicode_compatible
class AccidentHistory(models.Model):
    user = models.OneToOneField(User)
    description_and_location = models.TextField(blank=True)
    road_condition = models.CharField(max_length=10,
                                      choices=ROAD_CONDITION_CHOICES,
                                      blank=True)
    anticipation_of_accident = models.NullBooleanField()
    time_of_the_day = models.DateTimeField(blank=True)
    patient_vehicle = models.CharField(max_length=30, blank=True)
    patient_vehicle_speed = models.IntegerField(blank=True)
    other_vehicle = models.CharField(max_length=30, blank=True)
    other_vehicle_speed = models.IntegerField(blank=True)
    collision_type = models.CharField(max_length=30,
                                      choices=COLLISION_TYPE_CHOICES,
                                      blank=True)
    vehicle_towed = models.NullBooleanField()
    impact_with_objects = models.CharField(max_length=50, blank=True)
    exit_from_vehicle = models.CharField(max_length=30,
                                         choices=EXIT_FROM_VEHICLE_CHOICES,
                                         blank=True)
    loss_of_consciousness = models.NullBooleanField()
    safety_equipment = models.NullBooleanField()
    airbag_deployed = models.NullBooleanField()
    driver = models.NullBooleanField()
    passengers = models.ManyToManyField(PassengerLocation)
    dominant_hand = models.CharField(max_length=20,
                                     choices=DOMINANT_HAND_CHOICES,
                                     blank=True)
    body_part_collision = models.ManyToManyField(BodyPart, blank=True)

    def __str__(self):
        return 'Health history for ' + self.user.first_name
        + ' ' + self.user.last_name
