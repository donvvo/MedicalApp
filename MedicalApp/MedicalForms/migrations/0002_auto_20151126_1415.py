# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accidenthistory',
            name='today_date',
        ),
        migrations.RemoveField(
            model_name='healthhistory',
            name='today_date',
        ),
        migrations.RemoveField(
            model_name='tmjscreening',
            name='today_date',
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 19, 15, 3, 200707, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 19, 15, 7, 986135, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lowerextremity',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 19, 15, 12, 119101, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tmjscreening',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 19, 15, 17, 978381, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upperextremity',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 19, 15, 23, 86501, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
