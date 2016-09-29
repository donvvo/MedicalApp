# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views

from . import views


urlpatterns = [
    # Patient forms
    url(r'^patient-information/(?P<user_id>[\d]+)/$', views.PatientInformationView.as_view(),
        name="patient_info"),
    url(r'^health-history/(?P<user_id>[\d]+)/$', views.HealthHistoryView.as_view(),
        name="health_history"),
    url(r'^accident-history/(?P<user_id>[\d]+)/$', views.AccidentHistoryView.as_view(),
        name="accident_history"),
    url(r'^tmj-screening/(?P<user_id>[\d]+)/$', views.TMJScreeningView.as_view(),
        name="tmj-screening"),
    url(r'^lower-extremity/(?P<user_id>[\d]+)/$', views.LowerExtremityView.as_view(),
        name="lower-extremity"),
    url(r'^upper-extremity/(?P<user_id>[\d]+)/$', views.UpperExtremityView.as_view(),
        name="upper-extremity"),
    url(r'^neck-disability/(?P<user_id>[\d]+)/$', views.NeckDisabilityView.as_view(),
        name="neck-disability"),
    url(r'^patient-satisfaction-survey/(?P<user_id>[\d]+)/$', views.PatientSatisfactionSurveyView.as_view(),
        name="patient-satisfaction-survey"),


    # Patient Consent forms
    url(r'^chiropractic-treatment/(?P<user_id>[\d]+)/$', views.ChiropracticTreatmentView.as_view(),
        name="chiropractic-treatment"),
    url(r'^physiotherapy-treatment/(?P<user_id>[\d]+)/$', views.PhysiotherapyTreatmentView.as_view(),
        name="physiotherapy-treatment"),
    url(r'^massage-treatment/(?P<user_id>[\d]+)/$', views.MassageTreatmentView.as_view(),
        name="massage-treatment"),
    url(r'^medical-authorization/(?P<user_id>[\d]+)/$', views.MedicalAuthorizationView.as_view(),
        name="medical-authorization"),
    url(r'^exchange-information/(?P<user_id>[\d]+)/$', views.ExchangeInformationView.as_view(),
        name="exchange-information"),
    url(r'^authorization-and-direction/(?P<user_id>[\d]+)/$', views.AuthorizationAndDirectionView.as_view(),
        name="authorization-and-direction"),
    url(r'^section47/(?P<user_id>[\d]+)/$', views.Section47View.as_view(),
        name="section47"),
    url(r'^statutory-accidents-benefits/(?P<user_id>[\d]+)/$', views.StatutoryAccidentsBenefitsView.as_view(),
        name="statutory-accidents-benefits"),

    # Doctor forms
    url(r'^plan-of-management/(?P<user_id>[\d]+)/$', views.PlanOfManagementView.as_view(),
        name="plan-of-management"),
    url(r'^patient-discharge/(?P<user_id>[\d]+)/$', views.PatientDischargeView.as_view(),
        name="patient-discharge"),
    url(r'^acute-concussion-eval/(?P<user_id>[\d]+)/$', views.AcuteConcussionEvaluationView.as_view(),
        name="acute-concussion-eval"),
    url(r'^assessment/(?P<user_id>[\d]+)/$', views.AssessmentView.as_view(),
        name="assessment"),
    url(r'^subjective-evaluation/(?P<user_id>[\d]+)/$', views.SubjectiveEvaluationView.as_view(), name="subjective_eval"),
    url(r'^MVA-intake/$', views.MVAIntakeView.as_view(), name="MVA_intake"),
    url(r'^report-of-findings/(?P<user_id>[\d]+)/$', views.ReportOfFindingsView.as_view(),
        name="report-of-findings"),
    url(r'^patient-specific-funtional-scale/(?P<user_id>[\d]+)/$', views.PatientSpecificView.as_view(),
        name="patient-specific-funtional-scale"),
    url(r'^attendance-sheet/(?P<user_id>[\d]+)/$', views.AttendanceSheetView.as_view(),
        name="attendance-sheet"),
    url(r'^attendance-sheet/(?P<user_id>[\d]+)/treatmentplan/add$', views.TreatmentPlanAddView.as_view(),
        name="treatmentplan-add"),
    url(r'^attendance-sheet/(?P<user_id>[\d]+)/datesignature/add$', views.DateSignatureAddView.as_view(),
        name="datesignature-add"),

    # Summary forms
    url(r'^summary/$', views.TemplateView.as_view(template_name='medicalforms/table_summary/summary_list.html'),
        name="summary-of-questionnaire"),
    url(r'^summary/lower-extremity/$', views.LowerExtremitySummaryView.as_view(),
        name="summary-lower-extremity"),
    url(r'^summary/upper-extremity/$', views.UpperExtremitySummaryView.as_view(),
        name="summary-upper-extremity"),
    url(r'^summary/neck-disability/$', views.NeckDisabilitySummaryView.as_view(),
        name="summary-neck-disability"),



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
