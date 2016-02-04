from django.views.generic import ListView

from braces.views import LoginRequiredMixin

from .models import Notification


class NotificationView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = "notifications/view_notifications.html"
    raise_exception = True

    def get_queryset(self):
        return self.model.objects.filter(target=self.request.user).all()