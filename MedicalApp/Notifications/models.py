from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Notification(models.Model):
    subject = models.ForeignKey('users.User', related_name='subject')
    action_type = models.CharField(max_length=30)
    action = models.CharField(max_length=200)
    target = models.ForeignKey('users.User', related_name='target')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Subject: ' + str(self.subject) + ', action: ' + str(self.action) + ', target: ' + str(self.target)
