from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator

from braces.views import LoginRequiredMixin, GroupRequiredMixin

from MedicalApp.utils import user_passes_test_with_kwargs
from .models import ChiropracticTreatment
from .forms import ChiropracticTreatmentForm


def owner_or_doctors(user, **kwargs):
    user_id = int(kwargs['user_id'])
    return user.pk == user_id or user.groups.filter(name="Doctors").exists()


class DoctorOnlyMixin(LoginRequiredMixin, GroupRequiredMixin):
    group_required = 'Doctors'
    raise_exception = True


class PatientFormBaseView(LoginRequiredMixin, UpdateView):
    # Only allows access to doctors or patients to their own forms
    @method_decorator(user_passes_test_with_kwargs(owner_or_doctors))
    def dispatch(self, request, *args, **kwargs):
        self.user_id = int(kwargs['user_id'])
        return super(PatientFormBaseView, self). dispatch(request, *args, **kwargs)

    def get_object(self):
        objects = self.model.objects.filter(pk=self.user_id)
        if objects.exists():
            return objects.get()
        else:
            return self.model(pk=self.user_id)


class ChiropracticTreatmentView(PatientFormBaseView):
    template_name = 'medicalforms/chiropractic_consent.html'
    model = ChiropracticTreatment
    form_class = ChiropracticTreatmentForm

    def get_success_url(self):
        return reverse_lazy('users:patient_profile', kwargs={'username': self.request.user.username})
