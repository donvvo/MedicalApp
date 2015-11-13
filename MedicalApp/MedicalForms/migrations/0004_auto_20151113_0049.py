# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0003_auto_20151113_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earlysign',
            name='choice',
            field=models.CharField(max_length=40),
        ),
    ]
