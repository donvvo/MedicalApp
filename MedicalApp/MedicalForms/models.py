from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from MedicalApp.users.models import User


# Patient information form choices
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)
OCCUPATIONAL_STATUS_CHOICES = (
    ('Full-time', 'Full-time'),
    ('Part-time', 'Part-time'),
    ('Modified Duties', 'Modified Duties'),
    ('NotReturned', 'NotReturned'),
    ('Unemployed', 'Unemployed'),
    ('Retired', 'Retired')
)
JOB_REQUIREMENTS_CHOICES = (
    ('Mainly sitting', 'Mainly sitting'),
    ('Mainly standing', 'Mainly standing'),
    ('Light labour', 'Light labour'),
    ('Heavy labour', 'Heavy labour')
)
MARITAL_STATUS_CHOICES = (
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Divorced', 'Divorced'),
    ('Common Law', 'Common Law')
)

# Patient information form
@python_2_unicode_compatible
class General(models.Model):
    user = models.OneToOneField(User)
    today_date = models.DateTimeField(auto_now_add=True, blank=True)
    accident_date = models.DateTimeField(blank=True)
    date_of_birth = models.DateTimeField(blank=True)
    name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    first_language = models.CharField(max_length=100, blank=True)
    home_phone = models.CharField(max_length=20, blank=True)
    mobile_phone = models.CharField(max_length=20, blank=True)
    work_phone = models.CharField(max_length=20, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    modified_duties_availability = models.NullBooleanField()
    occupational_status = models.CharField(max_length=20,
                                           choices=OCCUPATIONAL_STATUS_CHOICES,
                                           blank=True)
    job_requirements = models.CharField(max_length=20,
                                        choices=JOB_REQUIREMENTS_CHOICES,
                                        blank=True)
    marital_status = models.CharField(max_length=20,
                                      choices=MARITAL_STATUS_CHOICES,
                                      blank=True)
    number_of_children = models.IntegerField(blank=True)
    ages = models.CharField(max_length=100, blank=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True)
    emergency_contact_relationship = models.CharField(max_length=20, blank=True)




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


@python_2_unicode_compatible
class BodyPart(models.Model):
    choice = models.CharField(max_length=20)


# Accident history
@python_2_unicode_compatible
class AccidentHistory(models.Model):
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
                                         chocies=EXIT_FROM_VEHICLE_CHOICES,
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
