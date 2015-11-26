# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0005_auto_20151126_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmjscreening',
            name='pain',
            field=models.ManyToManyField(to='MedicalForms.Pain', null=True),
        ),
        migrations.AlterField(
            model_name='tmjscreening',
            name='symptom',
            field=models.ManyToManyField(to='MedicalForms.Symptom', null=True),
        ),
    ]
