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
class PatientInformation(models.Model):
    user = models.OneToOneField(User)
    today_date = models.DateTimeField(auto_now_add=True, blank=True)
    accident_date = models.DateTimeField(blank=True)
    date_of_birth = models.DateTimeField(blank=True)
    name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10,
                              choices=GENDER_CHOICES,
                              blank=True)
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
    ages = models.IntegerField(blank=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True)
    emergency_contact_relationship = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return 'Patient information for ' + self.user.first_name
        + ' ' + self.user.last_name
