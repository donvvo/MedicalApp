# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0003_doctorspecialty'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='clinic',
            field=models.ForeignKey(default='Test Clinic 1', to='MedicalAppointments.Clinic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialty',
            field=models.ForeignKey(default='Physiotherapist', to='MedicalAppointments.DoctorSpecialty'),
            preserve_default=False,
        ),
    ]
