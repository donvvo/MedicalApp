# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0006_auto_20151126_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmjscreening',
            name='pain',
            field=models.ManyToManyField(to='MedicalForms.Pain', blank=True),
        ),
        migrations.AlterField(
            model_name='tmjscreening',
            name='symptom',
            field=models.ManyToManyField(to='MedicalForms.Symptom', blank=True),
        ),
    ]
