# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0009_auto_20160203_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorspecialty',
            name='image_url',
            field=models.CharField(default=b'img/features/featured-2.jpg', max_length=50),
        ),
    ]
