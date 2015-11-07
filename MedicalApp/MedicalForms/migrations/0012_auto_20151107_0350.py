# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MedicalForms', '0011_auto_20151027_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cervical',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('neutral_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('neutral_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('jackson_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('jackson_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('spurling_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('spurling_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('hermitte_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('hermitte_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('julls_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('julls_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('adson_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('adson_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('wrights_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('wrights_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('edens_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('edens_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('easts_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('easts_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('doorbell_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('doorbell_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
            ],
        ),
        migrations.CreateModel(
            name='Elbow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flexion_l', models.IntegerField(blank=True)),
                ('flexion_r', models.IntegerField(blank=True)),
                ('extension_l', models.IntegerField(blank=True)),
                ('extension_r', models.IntegerField(blank=True)),
                ('supination_l', models.IntegerField(blank=True)),
                ('supination_r', models.IntegerField(blank=True)),
                ('pronation_l', models.IntegerField(blank=True)),
                ('pronation_r', models.IntegerField(blank=True)),
                ('cozens_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('cozens_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('reverse_cozens_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('reverse_cozens_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('tinels_elbow_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('tinels_elbow_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('tinels_wrist_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('tinels_wrist_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('varus_stress_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('varus_stress_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('valgus_stress_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('valgus_stress_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
            ],
        ),
        migrations.CreateModel(
            name='Knee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flexion_l', models.IntegerField(blank=True)),
                ('flexion_r', models.IntegerField(blank=True)),
                ('extension_l', models.IntegerField(blank=True)),
                ('extension_r', models.IntegerField(blank=True)),
                ('internal_rot_l', models.IntegerField(blank=True)),
                ('internal_rot_r', models.IntegerField(blank=True)),
                ('external_rot_l', models.IntegerField(blank=True)),
                ('external_rot_r', models.IntegerField(blank=True)),
                ('varus_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('varus_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('valgus_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('valgus_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('anterior_drawer_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('anterior_drawer_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('posterior_drawer_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('posterior_drawer_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('joint_line_tenderness_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('joint_line_tenderness_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('thesselis_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('thesselis_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('mcmurrays_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('mcmurrays_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('patello_femoral_grind_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('patello_femoral_grind_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('obers_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('obers_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('nobles_comp_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('nobles_comp_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('patellar_comp_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('patellar_comp_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
            ],
        ),
        migrations.CreateModel(
            name='Lumbar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slr_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('slr_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('braggarts_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('braggarts_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('bowstring_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('bowstring_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('thomas_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('thomas_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('fig4_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('fig4_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('si_comp_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('si_comp_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('yeomans_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('yeomans_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('hibbs_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('hibbs_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('gillets_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('gillets_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('sorensons_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
            ],
        ),
        migrations.CreateModel(
            name='MVAIntake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('today_date', models.DateTimeField(auto_now_add=True)),
                ('gait', models.CharField(blank=True, max_length=10, choices=[(b'Antalgic', b'Antalgic'), (b'Normal', b'Normal')])),
                ('assistive_devices', models.CharField(max_length=100, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shoulder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flexion_l', models.IntegerField(blank=True)),
                ('flexion_r', models.IntegerField(blank=True)),
                ('extension_l', models.IntegerField(blank=True)),
                ('extension_r', models.IntegerField(blank=True)),
                ('abduction_l', models.IntegerField(blank=True)),
                ('abduction_r', models.IntegerField(blank=True)),
                ('internal_rotation_l', models.IntegerField(blank=True)),
                ('internal_rotation_r', models.IntegerField(blank=True)),
                ('external_rotation_l', models.IntegerField(blank=True)),
                ('external_rotation_r', models.IntegerField(blank=True)),
                ('horizontal_abd_l', models.IntegerField(blank=True)),
                ('horizontal_abd_r', models.IntegerField(blank=True)),
                ('horizontal_add_l', models.IntegerField(blank=True)),
                ('horizontal_add_r', models.IntegerField(blank=True)),
                ('scapulocostal_rhythm_l', models.IntegerField(blank=True)),
                ('scapulocostal_rhythm_r', models.IntegerField(blank=True)),
                ('speeds_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('speeds_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('yergasons_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('yergasons_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('empty_can_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('empty_can_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('hornblowers_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('hornblowers_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('hawkins_kennedy_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('hawkins_kennedy_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('neers_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('neers_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('obriens_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('obriens_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('crank_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('crank_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('load_and_shift_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('load_and_shift_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('anterior_apprehension_l', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('anterior_apprehension_r', models.CharField(blank=True, max_length=1, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('main_form', models.OneToOneField(to='MedicalForms.MVAIntake')),
            ],
        ),
        migrations.AddField(
            model_name='lumbar',
            name='main_form',
            field=models.OneToOneField(to='MedicalForms.MVAIntake'),
        ),
        migrations.AddField(
            model_name='knee',
            name='main_form',
            field=models.OneToOneField(to='MedicalForms.MVAIntake'),
        ),
        migrations.AddField(
            model_name='elbow',
            name='main_form',
            field=models.OneToOneField(to='MedicalForms.MVAIntake'),
        ),
        migrations.AddField(
            model_name='cervical',
            name='main_form',
            field=models.OneToOneField(to='MedicalForms.MVAIntake'),
        ),
    ]
