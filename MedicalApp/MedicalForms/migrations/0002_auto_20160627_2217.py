# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinformation',
            name='chest_abs_type',
            field=MedicalForms.utils.MySelectField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='head_pain_type',
            field=MedicalForms.utils.MySelectField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='lower_back_type',
            field=MedicalForms.utils.MySelectField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='lower_extremities_type',
            field=MedicalForms.utils.MySelectField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='neck_type',
            field=MedicalForms.utils.MySelectField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='upper_extremities_type',
            field=MedicalForms.utils.MySelectField(max_length=30, blank=True),
        ),
    ]
