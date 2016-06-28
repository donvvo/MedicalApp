# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0003_auto_20160627_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='PainChoices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='pain',
            field=models.ManyToManyField(to='MedicalForms.PainChoices', blank=True),
        ),
    ]
