# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0014_auto_20151118_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accidenthistory',
            name='body_part_collision',
            field=models.ManyToManyField(to='MedicalForms.BodyPart', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='passengers',
            field=models.ManyToManyField(to='MedicalForms.PassengerLocation', null=True, blank=True),
        ),
    ]
