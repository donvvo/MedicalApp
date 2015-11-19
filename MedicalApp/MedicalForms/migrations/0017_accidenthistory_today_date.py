# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0016_auto_20151118_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='accidenthistory',
            name='today_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 19, 0, 23, 44, 909189, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
