# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0009_auto_20151126_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planofmanagement',
            name='today_date',
        ),
        migrations.AddField(
            model_name='planofmanagement',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 27, 0, 11, 54, 726539, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
