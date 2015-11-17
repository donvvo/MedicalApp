# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0009_auto_20151115_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='name',
            field=MedicalForms.utils.MyCharField(max_length=100, serialize=False, primary_key=True),
        ),
    ]
