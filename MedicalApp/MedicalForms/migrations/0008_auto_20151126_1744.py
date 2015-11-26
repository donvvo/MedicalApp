# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0007_auto_20151126_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accidenthistory',
            name='time_of_the_day',
            field=MedicalForms.utils.MyTimeField(null=True, blank=True),
        ),
    ]
