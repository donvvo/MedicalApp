from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest, HttpResponse

from django.shortcuts import redirect, render_to_response
from django.views.generic import DetailView, ListView
import json

from braces.views import LoginRequiredMixin

from .models import Booking, DoctorSpecialty, Clinic, Doctor


# Create your views here.
class AppointmentView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "medicalappointments/appointment.html"

    def dispatch(self, request, *args, **kwargs):
        # Only patients can view
        if self.request.user.groups.filter(name="Patients").exists():
            print 'yes'
            return super(AppointmentView, self).dispatch(request,
                                                         *args, **kwargs)
        else:
            redirect_url = reverse("users:~redirect")
            return redirect(redirect_url)

    def get_queryset(self):
        bookings = self.model.objects.filter(patient=self.request.user.patient).all()
        return bookings


class NewAppointmentView(LoginRequiredMixin, ListView):
    model = DoctorSpecialty
    template_name = "medicalappointments/new_appointment.html"


def get_clinics(request):
    if request.method == 'GET':
        specialty = request.GET.get('specialty')
        doctors = Doctor.objects.filter(specialty__specialty=specialty)
        clinics = [d.clinic for d in doctors]
        return HttpResponse(serializers.serialize("json", clinics), content_type="application/json")
    return HttpResponseBadRequest()
