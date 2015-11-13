# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views

from . import views


urlpatterns = [
    # Patient information
    url(r'^patient-information/(?P<user_id>[\d]+)/$', views.PatientInformationView.as_view(),
        name="patient_info"),

    url(r'^health-history/(?P<user_id>[\d]+)/$', views.HealthHistoryView.as_view(),
        name="health_history"),
    url(r'^accident-history/(?P<user_id>[\d]+)/$', views.AccidentHistoryView.as_view(),
        name="accident_history"),
    url(r'^tmj-screening/(?P<user_id>[\d]+)/$', views.TMJScreeningView.as_view(),
        name="tmj-screening"),

    url(r'^acute-concussion-eval/(?P<user_id>[\d]+)/$', views.AcuteConcussionEvaluationView.as_view(),
        name="acute-concussion-eval"),
    url(r'^subjective-evaluation/$', views.SubjectiveEvaluationView.as_view(), name="subjective_eval"),
    url(r'^assessment/$', views.AssessmentView.as_view(), name="assessment"),
    url(r'^MVA-intake/$', views.MVAIntakeView.as_view(), name="MVA_intake"),

    # Report of Findings
    url(r'^report-of-findings/(?P<pk>[\d]+)/$', views.ReportOfFindingsView.as_view(),
        name="report_of_findings"),
    url(r'^report-of-findings/(?P<pk>[\d]+)/edit/$', views.ReportOfFindingsEditView.as_view(),
        name="report_of_findings_edit"),
    url(r'^report-of-findings/list/$', views.ReportOfFindingsListView.as_view(),
        name="report_of_findings_list"),
    url(r'^report-of-findings/(?P<pk>[\d]+)/new/$', views.ReportOfFindingsCreateView.as_view(),
        name="report_of_findings_new"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request),
        url(r'^403/$', default_views.permission_denied),
        url(r'^404/$', default_views.page_not_found),
        url(r'^500/$', default_views.server_error),
    ]