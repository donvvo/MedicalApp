# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import MedicalForms.utils
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0010_auto_20151126_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='acuteconcussionevaluation',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 1, 45, 19, 544707, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acuteconcussionevaluation',
            name='time_of_injury',
            field=MedicalForms.utils.MyTimeField(null=True, blank=True),
        ),
    ]
