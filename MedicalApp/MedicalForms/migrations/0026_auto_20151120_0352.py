# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0025_auto_20151120_0351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accidenthistory',
            old_name='impact_with_objects_boolean',
            new_name='impact_with_objects',
        ),
    ]
