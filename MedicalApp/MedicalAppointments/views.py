from django.views.generic import DetailView, ListView

from braces.views import LoginRequiredMixin

from .models import Booking

# Create your views here.
class AppointmentView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "medicalappointments/appointment.html"

    def get_queryset(self):
        bookings = self.model.objects.filter(patient=self.request.user.patient).all()
        print bookings
        return bookings