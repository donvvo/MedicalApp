# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0004_auto_20151113_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redflags',
            name='choice',
            field=models.CharField(max_length=40),
        ),
    ]
