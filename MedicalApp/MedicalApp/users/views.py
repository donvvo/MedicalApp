# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from braces.views import LoginRequiredMixin
from allauth.account.views import LoginView, SignupView
from allauth.account.utils import complete_signup
from allauth.account import app_settings

from .models import User


class UserLoginView(LoginView):
    pass


class MyBaseSignupView(SignupView):
    def form_valid(self, form):
        # TODO:// move this to somewhere else
        # Create two user groups: patients and doctors
        Group.objects.get_or_create(name='Patients')
        Group.objects.get_or_create(name='Doctors')


class UserSignupView(MyBaseSignupView):
    def form_valid(self, form):
        super(UserSignupView, self).form_valid(form)
        user = form.save(self.request)
        user.add_to_patients_group()
        return complete_signup(self.request, user,
                               app_settings.EMAIL_VERIFICATION,
                               self.get_success_url())


class DoctorSignupView(MyBaseSignupView):
    def form_valid(self, form):
        super(UserSignupView, self).form_valid(form)
        user = form.save(self.request)
        user.add_to_doctors_group()
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
        return reverse("patient_profile",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"
