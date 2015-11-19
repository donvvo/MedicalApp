from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from .utils import *
from MedicalAppointments.models import Patient


# Accident history choices
FFS_POC_CHOICES = (
    ('FFS', 'FFS'),
    ('POC', 'POC')
)
ICE_HEAT_CHOICES = (
    ('ICE', 'ICE'),
    ('HEAT', 'HEAT')
)
ULTRASOUND_CHOICES = (
    ('1Mhz', '1Mhz'),
    ('3Mhz', '3Mhz')
)
IFC_CHOICES = (
    ('100-200 Hz', '100-200 Hz'),
    ('80-120 Hz', '80-120 Hz'),
    ('1-120 Hz', '1-120 Hz'),
    ('1-10 Hz', '1-10 Hz'),
    ('5-50 Hz', '5-50 Hz'),
)


# Accident history
@python_2_unicode_compatible
class PlanOfManagement(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    today_date = models.DateTimeField(auto_now_add=True)
    name = MyCharField(max_length=50)
    start_date = MyDateTimeField()
    end_date = MyDateTimeField()
    ffs_poc = MySelectField(max_length=10, choices=FFS_POC_CHOICES)
    poc_detail = MyCharField(max_length=50)
    duration_week = MyIntegerField()
    for_week = MyIntegerField()
    acu_mass = MyIntegerField()
    acu_week = MyIntegerField()
    acu_for_week = MyIntegerField()

    diagnosis_1 = MyCharField(max_length=100)
    diagnosis_2 = MyCharField(max_length=100)
    diagnosis_3 = MyCharField(max_length=100)
    diagnosis_4 = MyCharField(max_length=100)
    diagnosis_5 = MyCharField(max_length=100)
    dob = MyDateTimeField()
    claim_number = MyIntegerField()

    ice_heat = MySelectField(max_length=10, choices=ICE_HEAT_CHOICES)
    ice_heat_region = MyCharField(max_length=100)
    laser = MyIntegerField()
    laser_region = MyCharField(max_length=100)
    ultrasound = MySelectField(max_length=10, choices=ULTRASOUND_CHOICES)
    ultrasound_percent = IntegerRangeField(min_value=0, max_value=100)
    ultrasound_w = MyIntegerField()
    ultrasound_min = MyIntegerField()
    ultrasound_region = MyCharField(max_length=100)
    ifc = MySelectField(max_length=30, choices=IFC_CHOICES)
    ifc_region = MyCharField(max_length=100)
    ems_russian = MyCharField(max_length=100)
    microcurrent = MyCharField(max_length=100)

    bike_time = MyIntegerField()
    bike_load = MyIntegerField()
    treadmill_time = MyIntegerField()
    treadmill_load = MyIntegerField()
    elliptical_time = MyIntegerField()
    elliptical_load = MyIntegerField()

    stt_region = MyCharField(max_length=100)
    mob_region = MyCharField(max_length=100)
    smt_region = MyCharField(max_length=100)

    neck_muscles = MyCharField(max_length=100)
    neck_exercies = MyCharField(max_length=100)
    shoulder_muscles = MyCharField(max_length=100)
    shoulder_exercies = MyCharField(max_length=100)
    forarm_muscles = MyCharField(max_length=100)
    forarm_exercies = MyCharField(max_length=100)
    ts_muscles = MyCharField(max_length=100)
    ts_exercies = MyCharField(max_length=100)
    ls_muscles = MyCharField(max_length=100)
    ls_exercies = MyCharField(max_length=100)
    hip_muscles = MyCharField(max_length=100)
    hip_exercies = MyCharField(max_length=100)
    thigh_muscles = MyCharField(max_length=100)
    thigh_exercies = MyCharField(max_length=100)
    lower_leg_muscles = MyCharField(max_length=100)
    lower_leg_exercies = MyCharField(max_length=100)
    ankle_muscles = MyCharField(max_length=100)
    ankle_exercies = MyCharField(max_length=100)
    core_muscles = MyCharField(max_length=100)
    core_exercies = MyCharField(max_length=100)

    notes = MyTextField()

    def __str__(self):
        return 'Plan of Management for ' + str(self.patient)