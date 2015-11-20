# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0028_tmjscreening_dob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tmjscreening',
            old_name='dob',
            new_name='doi',
        ),
    ]
