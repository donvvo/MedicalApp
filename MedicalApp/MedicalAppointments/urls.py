# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView

from .views import AppointmentView


urlpatterns = [
    url(r'^$', AppointmentView.as_view(), name="appointments"),
    url(r'^new/$', TemplateView.as_view(template_name='medicalappointments/new_appointment.html'), name="new_appointments"),
    url(r'^timetable/$', TemplateView.as_view(template_name='medicalappointments/timetable_doctor.html'), name="timetable_doctor"),
    url(r'^new/timetable$', TemplateView.as_view(template_name='medicalappointments/timetable_patient.html'), name="timetable_patient"),
]