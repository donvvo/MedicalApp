# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0015_auto_20151118_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accidenthistory',
            name='body_part_collision',
            field=models.ManyToManyField(to='MedicalForms.BodyPart', blank=True),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='passengers',
            field=models.ManyToManyField(to='MedicalForms.PassengerLocation', blank=True),
        ),
    ]
