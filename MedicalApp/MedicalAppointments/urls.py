# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import AppointmentView, NewAppointmentView, get_clinics, PatientTimetableView, save_booking,\
    DoctorTimetableView


urlpatterns = [
    url(r'^$', AppointmentView.as_view(), name="appointments"),
    url(r'^new/$', NewAppointmentView.as_view(), name="new_appointments"),
    url(r'^new/save/$', save_booking, name="save_booking"),
    url(r'^timetable/$', DoctorTimetableView.as_view(), name="timetable_doctor"),
    url(r'^new/timetable/(?P<clinic>[\w+]+)/(?P<specialty>\w+)/$', PatientTimetableView.as_view(), name="timetable_patient"),
    url(r'^clinics/$', get_clinics, name="get_clinics"),

]