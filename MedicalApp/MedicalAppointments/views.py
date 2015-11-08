import datetime
import pytz

from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.views.generic import DetailView, ListView
from django.utils import timezone

from braces.views import LoginRequiredMixin

from .models import Booking, DoctorSpecialty, Clinic, Doctor


# Create your views here.
class AppointmentView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "medicalappointments/appointment.html"

    def dispatch(self, request, *args, **kwargs):
        # Only patients can view
        if self.request.user.groups.filter(name="Patients").exists():
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
        clinics = list(set([d.clinic for d in doctors]))
        return HttpResponse(serializers.serialize("json", clinics), content_type="application/json")
    return HttpResponseBadRequest()


class PatientTimetableView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "medicalappointments/timetable_patient.html"

    def dispatch(self, request, *args, **kwargs):
        # Only patients can view
        if self.request.user.groups.filter(name="Patients").exists():
            return super(PatientTimetableView, self).dispatch(request,
                                                         *args, **kwargs)
        else:
            redirect_url = reverse("users:~redirect")
            return redirect(redirect_url)

    def get_queryset(self):
        clinic = self.kwargs.get('clinic', None).replace('+', ' ')
        bookings = self.model.objects.filter(clinic=clinic).all()
        return bookings

    def get_dates_from_now(self):
        today = timezone.now().date()
        dates = []
        for day_delta in range(7):
            dates.append(today + datetime.timedelta(days=day_delta))
        return dates

    def get_time_interval(self):
        start_hour = datetime.time(hour=6)
        end_hour = datetime.time(hour=17)
        interval = datetime.timedelta(minutes=30)
        time_interval = []
        dates = self.get_dates_from_now()

        first_row = []
        for day in dates:
            first_row.append(datetime.datetime.combine(day, start_hour))
        time_interval.append(first_row)

        while time_interval[-1][0].time() < end_hour:
            table_row = []
            for day in time_interval[-1]:
                table_row.append(day + interval)
            time_interval.append(table_row)

        return time_interval

    def compare_with_bookings(self, bookings):
        booking_time = [booking.time.replace(tzinfo=None) for booking in bookings]
        time_interval = self.get_time_interval()

        table = []
        for row in time_interval:
            table_row = []
            for column in row:
                if column in booking_time:
                    table_row.append([column, True])
                else:
                    table_row.append([column, False])
            table.append(table_row)

        return table

    def get_context_data(self, **kwargs):
        context = super(PatientTimetableView, self).get_context_data(**kwargs)
        context['table'] = self.compare_with_bookings(context['object_list'])
        context['clinic'] = self.kwargs.get('clinic', None).replace('+', ' ')

        return context


def save_booking(request):
    if request.method == 'POST':
        year = int(request.POST.get('year'))
        month = int(request.POST.get('month'))
        date = int(request.POST.get('date'))
        hour = int(request.POST.get('hour'))
        minute = int(request.POST.get('minute'))

        clinic_name = str(request.POST.get('clinic'))

        booking_time = datetime.datetime(year=year, month=month, day=date, hour=hour, minute=minute)

        timezone.make_aware(booking_time, timezone.get_current_timezone())

        clinic = Clinic(pk=clinic_name)
        doctor = Doctor(pk=10)
        booking = Booking(clinic=clinic, patient=request.user.patient, doctor=doctor, time=booking_time)
        booking.save()

        return HttpResponseRedirect(reverse("medical_appointments:appointments"))
    return HttpResponseBadRequest()
