from .models import Notification


def get_notifications(target):
    notifications = Notification.objects.filter(target=target).all()

    return notifications


def get_unread_notifications(target):
    notifications = Notification.objects.filter(target=target, read=False).all()

    return notifications