# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0006_auto_20151111_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='clinic',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='clinic',
            name='end_time',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='clinic',
            name='phone',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='clinic',
            name='start_time',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='address',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='postal_code',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
