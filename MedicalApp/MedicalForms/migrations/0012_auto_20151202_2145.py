# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0011_auto_20151202_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acuteconcussionevaluation',
            name='completed_date',
            field=MedicalForms.utils.MyDateTimeField(null=True, blank=True),
        ),
    ]
