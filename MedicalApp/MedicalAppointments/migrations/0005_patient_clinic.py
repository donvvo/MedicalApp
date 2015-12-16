# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0004_doctor_hcai'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='MedicalAppointments.Clinic', null=True),
        ),
    ]
