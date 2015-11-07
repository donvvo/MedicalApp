from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from .utils import MyCharField, MySelectField, IntegerRangeField
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
    user = models.ForeignKey(User)
    today_date = models.DateTimeField(auto_now_add=True, blank=True)
    accident_date = models.DateTimeField(blank=True)
    date_of_birth = models.DateTimeField(blank=True)
    gender = MySelectField(GENDER_CHOICES, max_length=10)
    address = MyCharField(max_length=200, placeholder='Address')
    city = MyCharField(max_length=100, placeholder='City')
    postal_code = MyCharField(max_length=10, placeholder='Postal Code')
    first_language = MyCharField(max_length=100, placeholder='First Language')
    home_phone = MyCharField(max_length=20, placeholder='Home Phone')
    mobile_phone = MyCharField(max_length=20, placeholder='Mobile Phone')
    work_phone = MyCharField(max_length=20, placeholder='Work Phone')
    occupation = MyCharField(max_length=100, placeholder='Occupation')
    modified_duties_availability = models.NullBooleanField()
    occupational_status = MySelectField(max_length=20, choices=OCCUPATIONAL_STATUS_CHOICES)
    job_requirements = MySelectField(max_length=20, choices=JOB_REQUIREMENTS_CHOICES)
    marital_status = MySelectField(max_length=20, choices=MARITAL_STATUS_CHOICES)
    number_of_children = IntegerRangeField(min_value=0, placeholder='Number of Children')
    ages = IntegerRangeField(min_value=1, placeholder='Ages')
    emergency_contact_name = MyCharField(max_length=100, placeholder='Emergency Contact Name')
    emergency_contact_phone = MyCharField(max_length=20, placeholder='Emergency Contact Phone')
    emergency_contact_relationship = MyCharField(max_length=20, placeholder='Emergency Contact Relationship')

    def __str__(self):
        return 'Patient information for ' + self.user.first_name
        + ' ' + self.user.last_name
