# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0005_auto_20151113_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='choice',
            field=models.CharField(max_length=40),
        ),
    ]
