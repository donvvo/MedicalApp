# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0010_auto_20151116_2112'),
        ('MedicalForms', '0022_auto_20151119_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanOfManagement',
            fields=[
                ('patient', models.OneToOneField(primary_key=True, serialize=False, to='MedicalAppointments.Patient')),
                ('today_date', models.DateTimeField(auto_now_add=True)),
                ('name', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('start_date', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('end_date', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('ffs_poc', MedicalForms.utils.MySelectField(max_length=10, blank=True)),
                ('poc_detail', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('duration_week', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('for_week', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('acu_mass', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('acu_week', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('acu_for_week', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('diagnosis_1', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('diagnosis_2', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('diagnosis_3', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('diagnosis_4', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('diagnosis_5', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('dob', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('claim_number', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('ice_heat', MedicalForms.utils.MySelectField(max_length=10, blank=True)),
                ('ice_heat_region', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('laser', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('laser_region', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('ultrasound', MedicalForms.utils.MySelectField(max_length=10, blank=True)),
                ('ultrasound_percent', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('ultrasound_w', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('ultrasound_min', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('ultrasound_region', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('ifc', MedicalForms.utils.MySelectField(max_length=30, blank=True)),
                ('ifc_region', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('ems_russian', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('microcurrent', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('bike_time', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('bike_load', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('treadmill_time', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('treadmill_load', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('elliptical_time', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('elliptical_load', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('stt_region', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('mob_region', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('smt_region', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('neck_muscles', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('neck_exercies', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('shoulder_muscles', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('shoulder_exercies', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('forarm_muscles', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('forarm_exercies', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('ts_muscles', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('ts_exercies', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('ls_muscles', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('ls_exercies', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('hip_muscles', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('hip_exercies', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('thigh_muscles', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('thigh_exercies', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('lower_leg_muscles', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('lower_leg_exercies', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('ankle_muscles', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('ankle_exercies', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('core_muscles', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('core_exercies', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('notes', MedicalForms.utils.MyTextField(blank=True)),
            ],
        ),
    ]
