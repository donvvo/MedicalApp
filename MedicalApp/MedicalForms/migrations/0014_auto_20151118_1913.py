# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0013_auto_20151118_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accidenthistory',
            name='passengers',
            field=models.ManyToManyField(to='MedicalForms.PassengerLocation', blank=True),
        ),
    ]
