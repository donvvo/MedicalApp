# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0002_auto_20151025_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='general',
            old_name='choices',
            new_name='choice',
        ),
        migrations.RenameField(
            model_name='musclejoint',
            old_name='choices',
            new_name='choice',
        ),
    ]
