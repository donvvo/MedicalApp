# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from allauth.account.views import logout

from . import views

from django.views.generic import TemplateView

urlpatterns = [
    # URL pattern for the UserLoginView
    url(
        regex=r'^login/$',
        view=views.UserLoginView.as_view(),
        name='account_login'
    ),

    url(
        regex=r'^settings/$',
        view=TemplateView.as_view(template_name="users/settings.html"),
        name='settings'
    ),

    # URL pattern for the DoctorSignupView
    url(
        regex=r'^signup/doctors/$',
        view=views.DoctorSignupView.as_view(),
        name='account_signup_doctors'
    ),

    # URL pattern for the UserSignupView
    url(
        regex=r'^signup/$',
        view=views.UserSignupView.as_view(),
        name='account_signup'
    ),

    url(r"^logout/$", logout, name="account_logout"),

    url(
        regex=r'^manage/$',
        view=views.ManageMainView.as_view(),
        name="manage_main"
    ),

    url(
        regex=r'^manage/patients$',
        view=views.PatientsListView.as_view(),
        name="patient_list"
    ),

    url(
        regex=r'^manage/doctors$',
        view=views.DoctorsListView.as_view(),
        name="doctors_list"
    ),

    url(
        regex=r'^manage/doctors/sendlink$',
        view=views.EmailDoctorView.as_view(),
        name="email_doctor"
    ),

    # URL pattern for the UserRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='account_redirect'
    ),

    # URL pattern for the PatientDoctorRedirectView
    url(
        regex=r'^(?P<user_id>[\w.@+-]+)/$',
        view=views.PatientDoctorRedirectView.as_view(),
        name='patient_doctor_redirect'
    ),

    # URL pattern for the UserDetailView
    url(
        regex=r'^patient/(?P<user_id>[\w.@+-]+)/$',
        view=views.PatientProfileView.as_view(),
        name='patient_profile'
    ),

    url(
        regex=r'^patient/(?P<user_id>[\d]+)/edit/$',
        view=views.UserSettingsView.as_view(),
        name='patient_profile_edit'
    ),

    url(
        regex=r'^doctor/(?P<user_id>[\d]+)/$',
        view=views.DoctorProfileView.as_view(),
        name='doctor_profile'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^doctor/(?P<user_id>[\d]+)/edit/$',
        view=views.DoctorProfileEditView.as_view(),
        name='doctor_profile_edit'
    ),
]
