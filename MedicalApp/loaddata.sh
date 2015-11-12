#!/bin/bash

python manage.py loaddata MedicalApp/fixtures/*
python manage.py loaddata MedicalAppointments/fixtures/*
python manage.py loaddata MedicalForms/fixtures/*
