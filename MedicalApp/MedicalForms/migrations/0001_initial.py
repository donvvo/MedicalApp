# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choices', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HealthHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('general', models.ManyToManyField(to='MedicalForms.General')),
            ],
        ),
        migrations.CreateModel(
            name='MuscleJoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choices', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='muscle_joint',
            field=models.ManyToManyField(to='MedicalForms.MuscleJoint'),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
