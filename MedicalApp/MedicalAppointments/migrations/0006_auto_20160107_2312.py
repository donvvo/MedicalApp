# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0005_patient_clinic'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='check_in',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='doctors_note',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='reasons',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='symptoms',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
    ]
