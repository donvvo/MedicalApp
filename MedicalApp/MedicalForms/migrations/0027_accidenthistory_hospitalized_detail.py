# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0026_auto_20151120_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='accidenthistory',
            name='hospitalized_detail',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
    ]
