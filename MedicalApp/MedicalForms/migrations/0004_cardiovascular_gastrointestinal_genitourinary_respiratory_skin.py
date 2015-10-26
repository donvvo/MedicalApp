# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0003_auto_20151025_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cardiovascular',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gastrointestinal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genitourinary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Respiratory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
    ]
