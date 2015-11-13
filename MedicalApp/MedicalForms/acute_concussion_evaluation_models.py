from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from .utils import *
from MedicalAppointments.models import Patient, Doctor


REPORTER_CHOICES = (
    ('Patient', 'Patient'),
    ('Parent', 'Parent'),
    ('Spouce', 'Spouce'),
    ('Other', 'Other')
)

LOCATION_CHOICES = (
    ('Frontal', 'Frontal'),
    ('Left Temp', 'Left Temp'),
    ('Right Temp', 'Right Temp'),
    ('Left Parietal', 'Left Parietal'),
    ('Right Parietal', 'Right Parietal'),
    ('Occipital', 'Occipital'),
    ('Neck', 'Neck'),
    ('Indirect Force', 'Indirect Force')
)

CAUSE_CHOICES = (
    ('MVC', 'MVC'),
    ('Pedestrian-MVC', 'Pedestrian-MVC'),
    ('Fall', 'Fall'),
    ('Assault', 'Assault'),
    ('Sports(specify)', 'Sports(specify)'),
    ('Other', 'Other'),
)

DURATION_CHOICES = (
    ('Days', 'Days'),
    ('Weeks', 'Weeks'),
    ('Months', 'Months'),
    ('Years', 'Years'),
)

FOLLOW_UP_CHOICES = (
    ('No Follow-Up Needed', 'No Follow-Up Needed'),
    ('Clinician Monitoring', 'Clinician Monitoring'),
)


@python_2_unicode_compatible
class EarlySignChoices(models.Model):
    choice = models.CharField(max_length=20)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class RedFlags(models.Model):
    choice = models.CharField(max_length=20)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class Diagnosis(models.Model):
    choice = models.CharField(max_length=20)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class Refferal(models.Model):
    choice = models.CharField(max_length=20)

    def __str__(self):
        return self.choice


@python_2_unicode_compatible
class AcuteConcussionEvaluation(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    dob = MyDateTimeField()

    date_of_injury = MyDateTimeField()
    reporter = MySelectField(max_length=10, choices=REPORTER_CHOICES)
    injury_description = MyCharField(max_length=100)
    evidence_of_blow = MyNullBooleanField()
    evidence_of_cranial_injury = MyNullBooleanField()
    location_of_impact = MySelectField(max_length=20, choices=LOCATION_CHOICES)
    cause = MySelectField(max_length=20, choices=CAUSE_CHOICES)
    sports_specify = MyCharField(max_length=50)
    others_specify = MyCharField(max_length=50)
    amnesia_before = MyNullBooleanField()
    amnesia_before_duration = MyCharField(max_length=10)
    amnesia_after = MyNullBooleanField()
    amnesia_after_duration = MyCharField(max_length=10)
    lost_of_consciousness = MyNullBooleanField()
    lost_of_consciousness_duration = MyCharField(max_length=10)
    early_signs = models.ManyToManyField(EarlySignChoices, blank=True)
    seizure = MyNullBooleanField()
    seizure_detail = MyCharField(max_length=10)

    headache = IntegerRangeField(min_value=0, max_value=1)
    nausea = IntegerRangeField(min_value=0, max_value=1)
    vomiting = IntegerRangeField(min_value=0, max_value=1)
    balance_problems = IntegerRangeField(min_value=0, max_value=1)
    dizziness = IntegerRangeField(min_value=0, max_value=1)
    visual_problems = IntegerRangeField(min_value=0, max_value=1)
    fatigue = IntegerRangeField(min_value=0, max_value=1)
    sensitivity_to_light = IntegerRangeField(min_value=0, max_value=1)
    sensitivity_to_noise = IntegerRangeField(min_value=0, max_value=1)
    numbness_and_tingling = IntegerRangeField(min_value=0, max_value=1)
    physical_total = IntegerRangeField(min_value=0, max_value=10)

    foggy = IntegerRangeField(min_value=0, max_value=1)
    slow_down = IntegerRangeField(min_value=0, max_value=1)
    difficulty_concentrating = IntegerRangeField(min_value=0, max_value=1)
    difficulty_remembering = IntegerRangeField(min_value=0, max_value=1)
    cognitive_total = IntegerRangeField(min_value=0, max_value=4)

    irritability = IntegerRangeField(min_value=0, max_value=1)
    sadness = IntegerRangeField(min_value=0, max_value=1)
    more_emotional = IntegerRangeField(min_value=0, max_value=1)
    nervousness = IntegerRangeField(min_value=0, max_value=1)
    emotional_total = IntegerRangeField(min_value=0, max_value=4)

    drowsiness = IntegerRangeField(min_value=0, max_value=1)
    sleeping_less = IntegerRangeField(min_value=0, max_value=1)
    sleeping_more = IntegerRangeField(min_value=0, max_value=1)
    trouble_falling_asleep = IntegerRangeField(min_value=0, max_value=1)
    sleep_total = IntegerRangeField(min_value=0, max_value=4)

    all_total = IntegerRangeField(min_value=0, max_value=22)

    excertion_physical = MyNullBooleanField()
    excertion_cognitive = MyNullBooleanField()

    overall_rating = IntegerRangeField(min_value=0, max_value=6)

    concussion_history = MyNullBooleanField()
    previous_number = IntegerRangeField(min_value=1)
    longest_duration = MySelectField(max_length=10, choices=DURATION_CHOICES)
    less_force_caused_reinjury = MyNullBooleanField()

    headache_history = MyNullBooleanField()
    prior_treatment = MyNullBooleanField()
    history_of_migraine = MyNullBooleanField()
    personal_family = MyCharField(max_length=100)

    learning_disabilities = MyNullBooleanField()
    attention_deficit = MyNullBooleanField()
    other_developmental = MyCharField(max_length=100)

    anxiety = MyNullBooleanField()
    depression = MyNullBooleanField()
    sleep_disorder = MyNullBooleanField()
    other_psychiatric = MyCharField(max_length=100)

    list_other_disorders = MyCharField(max_length=200)
    red_flags = models.ManyToManyField(RedFlags, blank=True)
    dignosis = models.ManyToManyField(Diagnosis, blank=True)
    follow_up = MySelectField(max_length=30, choices=FOLLOW_UP_CHOICES)
    refferal = models.ManyToManyField(Refferal, blank=True)
    refferal_others = MyCharField(max_length=50)

    doctor = models.ForeignKey(Doctor, blank=True, null=True)
    completed_date = MyDateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Accute Concussion Evaluation for ' + str(self.patient) + ' by ' + str(self.doctor)
