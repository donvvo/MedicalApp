# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import Group
from django.db import migrations, models


def create_groups(apps, schema_editor):
    # TODO:// move this to somewhere else
    # Create two user groups: patients and doctors
    Group.objects.get_or_create(name='Patients')
    Group.objects.get_or_create(name='Doctors')


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RunPython(create_groups),
    ]
