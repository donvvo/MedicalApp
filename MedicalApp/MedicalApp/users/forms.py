import logging

from django import forms
from allauth.account.forms import LoginForm

logger = logging.getLogger(__name__)


class UserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={
                                                  'type': 'email',
                                                  'class': 'form-control',
                                                  'placeholder': 'Email'})
        self.fields['login'].error_messages['required'] = \
            "Email is required."
        self.fields['password'].widget = forms.TextInput(attrs={
                                             'type': 'password',
                                             'class': 'form-control',
                                             'placeholder': 'Password'})
        self.fields['password'].error_messages['required'] = \
            "Password is required."