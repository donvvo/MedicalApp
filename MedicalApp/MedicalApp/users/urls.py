# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from allauth.account.views import logout

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),

    # URL pattern for the UserLoginView
    url(
        regex=r'^login/$',
        view=views.UserLoginView.as_view(),
        name='account_login'
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

    # URL pattern for the UserRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='account_redirect'
    ),

    # URL pattern for the PatientDoctorRedirectView
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.PatientDoctorRedirectView.as_view(),
        name='patient_doctor_redirect'
    ),

    # URL pattern for the UserDetailView
    url(
        regex=r'^patient/(?P<username>[\w.@+-]+)/$',
        view=views.PatientProfileView.as_view(),
        name='patient_profile'
    ),

    url(
        regex=r'^doctor/(?P<username>[\w.@+-]+)/$',
        view=views.DoctorProfileView.as_view(),
        name='doctor_profile'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^~settings/$',
        view=views.UserSettingsView.as_view(),
        name='user_settings'
    ),
]
