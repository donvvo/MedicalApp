# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='medicalappointments/appointment.html'), name="appointments"),
    url(r'^new/$', TemplateView.as_view(template_name='medicalappointments/new_appointment.html'), name="new_appointments"),
    url(r'^timetable/$', TemplateView.as_view(template_name='medicalappointments/timetable_doctor.html'), name="timetable_doctor"),
    url(r'^new/timetable$', TemplateView.as_view(template_name='medicalappointments/timetable_patient.html'), name="timetable_patient"),
]