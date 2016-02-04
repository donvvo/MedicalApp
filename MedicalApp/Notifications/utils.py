from .models import Notification


def get_notifications(target):
    notifications = Notification.objects.filter(target=target).all()

    return notifications