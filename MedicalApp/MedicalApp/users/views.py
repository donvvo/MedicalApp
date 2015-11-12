# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView
from django.shortcuts import redirect, get_object_or_404

from braces.views import LoginRequiredMixin
from allauth.account.views import LoginView, SignupView, FormView
from allauth.account.utils import complete_signup
from allauth.account import app_settings

from .models import User
from MedicalAppointments.models import Patient, Doctor
from .forms import UserSettingsForm, EmailDoctorForm


class HomeView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        if self.request.user.is_staff:
            return reverse("users:manage_main")
        elif self.request.user.groups.filter(name="Doctors").exists():
            return reverse("medical_appointments:timetable_doctor")
        else:
            return reverse("medical_appointments:appointments")


class UserLoginView(LoginView):
    pass


class UserSignupView(SignupView):
    def form_valid(self, form):
        user = form.save(self.request)
        user.add_to_patients_group()
        patient = Patient(user=user)
        patient.save()
        return complete_signup(self.request, user,
                               app_settings.EMAIL_VERIFICATION,
                               self.get_success_url())


class DoctorSignupView(SignupView):
    def form_valid(self, form):
        user = form.save(self.request)
        user.add_to_doctors_group()
        doctor = Doctor(user=user)
        doctor.save()
        return complete_signup(self.request, user,
                               app_settings.EMAIL_VERIFICATION,
                               self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(DoctorSignupView, self).get_context_data(**kwargs)
        context['doctors'] = True
        return context


class PatientProfileView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/patient_profile.html"


class DoctorProfileView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/doctor_profile.html"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:patient_doctor_redirect",
                       kwargs={"username": self.request.user.username})


class PatientDoctorRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, username):
        if self.request.user.groups.filter(name="Doctors").exists():
            return reverse("users:doctor_profile",
                       kwargs={"username": username})
        else:
            return reverse("users:patient_profile",
                           kwargs={"username": username})


class UserSettingsView(LoginRequiredMixin, UpdateView):
    form_class = UserSettingsForm
    template_name = 'users/user_settings.html'
    slug_field = "username"
    slug_url_kwarg = "username"

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:account_redirect")

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class ManageMainView(LoginRequiredMixin, TemplateView):
    template_name = "users/manage_main.html"

    def dispatch(self, request, *args, **kwargs):
        self.request.user.is_staff
        if self.request.user.is_staff:
            return super(ManageMainView, self).dispatch(request,
                                                         *args, **kwargs)
        else:
            redirect_url = reverse("users:account_redirect")
            return redirect(redirect_url)


class DoctorsListView(LoginRequiredMixin, ListView):
    model = Doctor
    template_name = "users/doctors_list.html"

    def dispatch(self, request, *args, **kwargs):
        self.request.user.is_staff
        if self.request.user.is_staff:
            return super(DoctorsListView, self).dispatch(request,
                                                         *args, **kwargs)
        else:
            redirect_url = reverse("users:account_redirect")
            return redirect(redirect_url)


class EmailDoctorView(LoginRequiredMixin, FormView):
    template_name = "users/email_doctor.html"
    form_class = EmailDoctorForm
    success_url = reverse_lazy('users:doctors_list')

    def dispatch(self, request, *args, **kwargs):
        self.request.user.is_staff
        if self.request.user.is_staff:
            return super(EmailDoctorView, self).dispatch(request,
                                                         *args, **kwargs)
        else:
            redirect_url = reverse("users:account_redirect")
            return redirect(redirect_url)

    def form_valid(self, form):
        signin_uri = self.request.build_absolute_uri(reverse("users:account_signup_doctors"))
        form.send_email(self.request.user.email, signin_uri)
        return super(EmailDoctorView, self).form_valid(form)