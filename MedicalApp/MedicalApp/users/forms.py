import logging

from django import forms
from allauth.account.forms import LoginForm, SignupForm

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


class UserSignupForm(SignupForm):
    first_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(
                                        attrs={'type': 'text',
                                               'class': 'form-control',
                                               'placeholder': 'First Name'}),
                                 error_messages={
                                    'required': "First name is required."
                                 })
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(
                                        attrs={'type': 'text',
                                               'class': 'form-control',
                                               'placeholder': 'Last Name'}),
                                error_messages={
                                    'required': "Last name is required."
                                })

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = \
            forms.TextInput(attrs={'type': 'email',
                            'class': 'form-control',
                            'placeholder': 'Email'})
        self.fields['email'].error_messages['required'] = \
            "Email is required."

        self.fields['password1'].widget = \
            forms.TextInput(attrs={
                            'class': 'form-control',
                            'type': 'password',
                            'placeholder': 'Password'})
        self.fields['password1'].error_messages['required'] = \
            "Password is required."

        self.fields['password2'].widget = \
            forms.TextInput(attrs={
                            'class': 'form-control',
                            'type': 'password',
                            'placeholder': 'Confirm Password'})
        self.fields['password2'].error_messages['required'] = \
            "Password confirmation is required."