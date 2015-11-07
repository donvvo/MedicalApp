# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0017_auto_20151107_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientinformation',
            name='email',
        ),
        migrations.RemoveField(
            model_name='patientinformation',
            name='name',
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='ages',
            field=MedicalForms.utils.IntegerRangeField(blank=True),
        ),
    ]
