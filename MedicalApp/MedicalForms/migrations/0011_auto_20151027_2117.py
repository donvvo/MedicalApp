# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0010_auto_20151027_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accidenthistory',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
