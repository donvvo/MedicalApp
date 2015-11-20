# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0027_accidenthistory_hospitalized_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmjscreening',
            name='dob',
            field=MedicalForms.utils.MyDateTimeField(null=True, blank=True),
        ),
    ]
