# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0005_auto_20151107_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='clinic',
            field=models.ForeignKey(default=b'Test Clinic 1', blank=True, to='MedicalAppointments.Clinic'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialty',
            field=models.ForeignKey(default=b'Chiropractor', blank=True, to='MedicalAppointments.DoctorSpecialty'),
        ),
    ]
