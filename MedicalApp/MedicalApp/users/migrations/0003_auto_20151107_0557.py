# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='images/', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
