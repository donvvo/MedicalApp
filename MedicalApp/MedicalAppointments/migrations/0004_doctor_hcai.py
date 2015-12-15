# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0003_remove_clinic_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='HCAI',
            field=MedicalForms.utils.MyCharField(max_length=30, blank=True),
        ),
    ]
