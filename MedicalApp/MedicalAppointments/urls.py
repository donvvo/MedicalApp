# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView

from .views import AppointmentView, NewAppointmentView, get_clinics, PatientTimetableView


urlpatterns = [
    url(r'^$', AppointmentView.as_view(), name="appointments"),
    url(r'^new/$', NewAppointmentView.as_view(), name="new_appointments"),
    url(r'^timetable/$', TemplateView.as_view(template_name='medicalappointments/timetable_doctor.html'), name="timetable_doctor"),
    url(r'^new/timetable/(?P<clinic>[\w.@+-]+)$', PatientTimetableView.as_view(), name="timetable_patient"),
    url(r'^clinics/$', get_clinics, name="get_clinics"),
]