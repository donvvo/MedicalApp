# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0015_auto_20151107_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinformation',
            name='gender',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
    ]
