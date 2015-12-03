# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0003_remove_clinic_email'),
        ('MedicalForms', '0002_auto_20151203_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headachequestions',
            name='today_date',
        ),
        migrations.RemoveField(
            model_name='headachequestions',
            name='user',
        ),
        migrations.RemoveField(
            model_name='otherquestions',
            name='today_date',
        ),
        migrations.RemoveField(
            model_name='otherquestions',
            name='user',
        ),
        migrations.RemoveField(
            model_name='othersubjectiveevaluationquestions',
            name='today_date',
        ),
        migrations.RemoveField(
            model_name='othersubjectiveevaluationquestions',
            name='users',
        ),
        migrations.RemoveField(
            model_name='peripheraljointbasequestions',
            name='today_date',
        ),
        migrations.RemoveField(
            model_name='peripheraljointbasequestions',
            name='user',
        ),
        migrations.AddField(
            model_name='headachequestions',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 7, 3, 35, 635217, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='headachequestions',
            name='patient',
            field=models.OneToOneField(default=4, to='MedicalAppointments.Patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='otherquestions',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 7, 4, 14, 249671, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='otherquestions',
            name='patient',
            field=models.OneToOneField(default=4, to='MedicalAppointments.Patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='othersubjectiveevaluationquestions',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 7, 4, 43, 943627, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='othersubjectiveevaluationquestions',
            name='patient',
            field=models.OneToOneField(default=4, to='MedicalAppointments.Patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peripheraljointbasequestions',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 7, 4, 54, 156226, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peripheraljointbasequestions',
            name='patient',
            field=models.OneToOneField(default=4, to='MedicalAppointments.Patient'),
            preserve_default=False,
        ),
    ]
