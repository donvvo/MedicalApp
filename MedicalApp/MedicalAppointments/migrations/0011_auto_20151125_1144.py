# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0010_auto_20151116_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='MedicalAppointments.Clinic', null=True),
        ),
    ]
