# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0013_auto_20151202_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acuteconcussionevaluation',
            name='completed_date',
            field=MedicalForms.utils.MyDateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='acuteconcussionevaluation',
            name='date_of_injury',
            field=MedicalForms.utils.MyDateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='acuteconcussionevaluation',
            name='dob',
            field=MedicalForms.utils.MyDateField(null=True, blank=True),
        ),
    ]
