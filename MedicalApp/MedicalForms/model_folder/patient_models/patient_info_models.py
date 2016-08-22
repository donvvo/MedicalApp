from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from ...utils import *
from MedicalAppointments.models import Patient

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
PAIN_TYPES = (
    ('Numbness', 'Numbness'),
    ('Pins and Needles', 'Pins and Needles'),
    ('Aching', 'Aching'),
    ('Burning', 'Burning'),
    ('Stabbing', 'Stabbing')
)

@python_2_unicode_compatible
class PainChoices(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


# Patient information form
@python_2_unicode_compatible
class PatientInformation(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    last_modified = models.DateTimeField(auto_now=True)
    accident_date = MyDateTimeField()
    date_of_birth = MyDateTimeField()
    gender = MySelectField(GENDER_CHOICES, max_length=10)
    address = MyCharField(max_length=200, placeholder='Address')
    city = MyCharField(max_length=100, placeholder='City')
    postal_code = MyCharField(max_length=10, placeholder='Postal Code')
    first_language = MyCharField(max_length=100, placeholder='First Language')
    translator_need = MyNullBooleanField()
    home_phone = MyCharField(max_length=20, placeholder='Home Phone')
    mobile_phone = MyCharField(max_length=20, placeholder='Mobile Phone')
    work_phone = MyCharField(max_length=20, placeholder='Work Phone')
    occupation = MyCharField(max_length=100, placeholder='Occupation')
    modified_duties_availability = MyNullBooleanField()
    occupational_status = MySelectField(max_length=20, choices=OCCUPATIONAL_STATUS_CHOICES)
    job_requirements = MySelectField(max_length=20, choices=JOB_REQUIREMENTS_CHOICES)
    marital_status = MySelectField(max_length=20, choices=MARITAL_STATUS_CHOICES)
    number_of_children = IntegerRangeField(min_value=0, placeholder='Number of Children')
    ages = MyCharField(max_length=20, placeholder='Ages')
    emergency_contact_name = MyCharField(max_length=100, placeholder='Emergency Contact Name')
    emergency_contact_phone = MyCharField(max_length=20, placeholder='Emergency Contact Phone')
    emergency_contact_relationship = MyCharField(max_length=20, placeholder='Emergency Contact Relationship')

    # Human body diagram
    pain = models.ManyToManyField(PainChoices, blank=True)

    head_pain_type = MySelectField(max_length=30, choices=PAIN_TYPES)
    upper_extremities_pain_type = MySelectField(max_length=30, choices=PAIN_TYPES)
    neck_pain_type = MySelectField(max_length=30, choices=PAIN_TYPES)
    chest_abs_pain_type = MySelectField(max_length=30, choices=PAIN_TYPES)
    lower_back_pain_type = MySelectField(max_length=30, choices=PAIN_TYPES)
    lower_extremities_pain_type = MySelectField(max_length=30, choices=PAIN_TYPES)

    head_pain_level = IntegerRangeField(min_value=0, max_value=10, placeholder="Intensity")
    upper_extremities_pain_level = IntegerRangeField(min_value=0, max_value=10, placeholder="Intensity")
    neck_pain_level =  IntegerRangeField(min_value=0, max_value=10, placeholder="Intensity")
    chest_abs_pain_level =  IntegerRangeField(min_value=0, max_value=10, placeholder="Intensity")
    lower_back_pain_level =  IntegerRangeField(min_value=0, max_value=10, placeholder="Intensity")
    lower_extremities_pain_level =  IntegerRangeField(min_value=0, max_value=10, placeholder="Intensity")

    # Current symptoms
    current_complaint_1 = MyCharField(max_length=100)
    current_complaint_2 = MyCharField(max_length=100)
    current_complaint_3 = MyCharField(max_length=100)
    current_complaint_4 = MyCharField(max_length=100)
    previous_injury = MyNullBooleanField()
    previous_injury_detail = MyCharField(max_length=100)
    previous_work_injury = MyNullBooleanField()
    previous_work_injury_detail = MyCharField(max_length=100)
    previous_sporting_injury = MyNullBooleanField()
    previous_sporting_injury_detail = MyCharField(max_length=100)
    previous_therapy = MyNullBooleanField()
    previous_therapy_detail = MyCharField(max_length=100)
    hospitalized = MyNullBooleanField()
    hospitalized_detail = MyCharField(max_length=100)
    previous_test = MyNullBooleanField()
    previous_test_detail = MyCharField(max_length=100)

    def __str__(self):
        return 'Patient information for ' + str(self.patient)
