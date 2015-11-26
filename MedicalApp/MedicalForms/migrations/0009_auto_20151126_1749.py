# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0008_auto_20151126_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorizationanddirection',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 22, 49, 3, 82884, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chiropractictreatment',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 22, 49, 14, 679397, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exchangeinformation',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 22, 49, 16, 774882, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='massagetreatment',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 22, 49, 18, 614638, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicalauthorization',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 22, 49, 20, 393409, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='physiotherapytreatment',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 22, 49, 22, 162575, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section47',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 22, 49, 23, 963429, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statutoryaccidentsbenefits',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 22, 49, 25, 766976, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
