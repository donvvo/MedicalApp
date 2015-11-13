from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from .utils import *
from MedicalApp.users.models import User


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
    user = models.ForeignKey(User)
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
    impact_with_objects = MyCharField(max_length=50)
    exit_from_vehicle = MySelectField(max_length=30,
                                         choices=EXIT_FROM_VEHICLE_CHOICES)
    loss_of_consciousness = MyNullBooleanField()
    safety_equipment = MyNullBooleanField()
    airbag_deployed = MyNullBooleanField()
    driver = MyNullBooleanField()
    passengers = models.ManyToManyField(PassengerLocation)
    dominant_hand = MySelectField(max_length=20,
                                     choices=DOMINANT_HAND_CHOICES)
    body_part_collision = models.ManyToManyField(BodyPart, blank=True)

    def __str__(self):
        return 'Health history for ' + self.user.first_name
        + ' ' + self.user.last_name