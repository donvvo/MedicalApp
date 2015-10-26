# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

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
        name='login'
    ),

    # URL pattern for the DoctorSignupView
    url(
        regex=r'^signup/doctors/$',
        view=views.DoctorSignupView.as_view(),
        name='signup_doctors'
    ),

    # URL pattern for the UserSignupView
    url(
        regex=r'^signup/$',
        view=views.UserSignupView.as_view(),
        name='signup'
    ),

    # URL pattern for the UserRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the UserDetailView
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.PatientProfileView.as_view(),
        name='patient_profile'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
]
