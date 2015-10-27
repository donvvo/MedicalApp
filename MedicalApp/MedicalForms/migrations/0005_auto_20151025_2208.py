# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0004_cardiovascular_gastrointestinal_genitourinary_respiratory_skin'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousConditions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='cardiovascular',
            field=models.ManyToManyField(to='MedicalForms.Cardiovascular'),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='gastrointestinal',
            field=models.ManyToManyField(to='MedicalForms.Gastrointestinal'),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='genitourinary',
            field=models.ManyToManyField(to='MedicalForms.Genitourinary'),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='respiratory',
            field=models.ManyToManyField(to='MedicalForms.Respiratory'),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='skin',
            field=models.ManyToManyField(to='MedicalForms.Skin'),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='PreviousConditions',
            field=models.ManyToManyField(to='MedicalForms.PreviousConditions'),
        ),
    ]
