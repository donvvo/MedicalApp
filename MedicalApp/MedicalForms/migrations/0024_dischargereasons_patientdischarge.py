# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0010_auto_20151116_2112'),
        ('MedicalForms', '0023_planofmanagement'),
    ]

    operations = [
        migrations.CreateModel(
            name='DischargeReasons',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PatientDischarge',
            fields=[
                ('patient', models.OneToOneField(primary_key=True, serialize=False, to='MedicalAppointments.Patient')),
                ('today_date', models.DateTimeField(auto_now_add=True)),
                ('initial_complaint', MedicalForms.utils.MyTextField(blank=True)),
                ('progress_to_date', MedicalForms.utils.MyTextField(blank=True)),
                ('reccurance_recommendation', MedicalForms.utils.MyTextField(blank=True)),
                ('risks_complications', MedicalForms.utils.MyTextField(blank=True)),
                ('schedule_date', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('communication', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('other_notes', MedicalForms.utils.MyTextField(blank=True)),
                ('clinician', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('sign_date', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('discharge_reason', models.ManyToManyField(to='MedicalForms.DischargeReasons', blank=True)),
            ],
        ),
    ]
