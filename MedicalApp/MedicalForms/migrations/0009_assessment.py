# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MedicalForms', '0008_auto_20151027_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('today_date', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateTimeField(blank=True)),
                ('visit_number', models.IntegerField(blank=True)),
                ('clinician', models.CharField(max_length=100, blank=True)),
                ('subjective_choices', models.CharField(blank=True, max_length=15, choices=[(b'Reg.', b'Reg.'), (b'Irreg.', b'Irreg.'), (b'Pain/Cramps', b'Pain/Cramps')])),
                ('subjective_description', models.TextField(blank=True)),
                ('assessment', models.TextField(blank=True)),
                ('objective', models.TextField(blank=True)),
                ('smt', models.TextField(blank=True)),
                ('stt', models.TextField(blank=True)),
                ('cardio', models.CharField(max_length=100, blank=True)),
                ('stretch', models.CharField(max_length=100, blank=True)),
                ('strength', models.CharField(max_length=100, blank=True)),
                ('ifc', models.CharField(max_length=100, blank=True)),
                ('u_s', models.CharField(max_length=100, blank=True)),
                ('heat', models.CharField(max_length=100, blank=True)),
                ('ice', models.CharField(max_length=100, blank=True)),
                ('ohter', models.TextField(blank=True)),
                ('education', models.TextField(blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
