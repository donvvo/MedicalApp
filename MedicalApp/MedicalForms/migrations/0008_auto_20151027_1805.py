# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0007_auto_20151027_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='headachequestions',
            old_name='users',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='lumbarspinequestions',
            old_name='users',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='otherquestions',
            old_name='users',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='peripheraljointbasequestions',
            old_name='users',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='thoracicspinequestions',
            old_name='users',
            new_name='user',
        ),
    ]
