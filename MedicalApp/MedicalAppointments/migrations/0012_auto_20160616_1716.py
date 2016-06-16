# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0011_patient_transportation_need'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='current_medications',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='past_medications',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
    ]
