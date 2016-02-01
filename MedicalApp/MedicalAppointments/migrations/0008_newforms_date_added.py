# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0007_newforms'),
    ]

    operations = [
        migrations.AddField(
            model_name='newforms',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 2, 52, 45, 830356, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
