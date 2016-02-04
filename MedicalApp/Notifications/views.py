from django.views.generic import ListView

from braces.views import LoginRequiredMixin

from .models import Notification
from .utils import get_notifications, get_unread_notifications


class NotificationView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = "notifications/view_notifications.html"
    raise_exception = True

    def get_queryset(self):
        return get_notifications(self.request.user)[:]

    def get_context_data(self, **kwargs):
        context = super(NotificationView, self).get_context_data(**kwargs)

        for notification in get_unread_notifications(self.request.user):
            notification.read = True
            notification.save()

        return context