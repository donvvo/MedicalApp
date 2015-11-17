# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.AppointmentView.as_view(), name="appointments"),
    url(r'^new/$', views.NewAppointmentView.as_view(), name="new_appointments"),
    url(r'^timetable/$', views.DoctorTimetableView.as_view(), name="timetable_doctor"),
    url(r'^new/timetable/(?P<clinic>[\w+]+)/(?P<specialty>\w+)/$', views.PatientTimetableView.as_view(), name="timetable_patient"),
    url(r'^clinics/.json$', views.get_clinics, name="get_clinics"),
    url(r'^clinics/list/$', views.ClinicListView.as_view(), name='clinic_list'),
    url(r'^clinics/(?P<clinicname>[\w.@+-]+)/$', views.ClinicProfileView.as_view(), name='clinic_profile'),
    url(r'^clinics/(?P<clinicname>[\w.@+-]+)/edit$', views.ClinicProfileEditView.as_view(), name='clinic_profile_edit'),
    url(r'^clinics/~create$', views.ClinicProfileCreateView.as_view(), name='clinic_profile_create')
]