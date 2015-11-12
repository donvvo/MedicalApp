# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0022_auto_20151112_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientinformation',
            name='id',
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='user',
            field=models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
