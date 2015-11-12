# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0023_auto_20151112_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinformation',
            name='accident_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='date_of_birth',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
