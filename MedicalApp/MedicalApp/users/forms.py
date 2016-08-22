import logging
import warnings

from django import forms
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.tokens import default_token_generator

from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm,\
     ResetPasswordKeyForm
from allauth.account import app_settings
from allauth.utils import (get_current_site, 
                                   build_absolute_uri)
from allauth.account.utils import user_pk_to_url_str
from allauth.account.adapter import (get_adapter,)
from allauth.account.app_settings import AuthenticationMethod

from .models import User
from MedicalAppointments.models import Doctor, Clinic, Patient

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


class PatientSignupForm(UserSignupForm):
    clinic = forms.ModelChoiceField(queryset=Clinic.objects.all(),
            required=False,
            widget=forms.Select(attrs={
                            'class': 'form-control'
                            }))


class DoctorSignupForm(UserSignupForm):
    HCAI = forms.CharField(max_length=30, required=False,
                                 widget=forms.TextInput(
                                        attrs={'type': 'text',
                                               'class': 'form-control',
                                               'placeholder': 'HCAI code'}))

class UserResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserResetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={
                                                  'type': 'email',
                                                  'class': 'form-control',
                                                  'placeholder': 'Email'})

    def save(self, request, **kwargs):
        current_site = get_current_site(request)
        email = self.cleaned_data["email"]
        token_generator = kwargs.get("token_generator",
                                     default_token_generator)

        def deprecated_site():
            warnings.warn("Context variable `site` deprecated, use"
                          "`current_site` instead", DeprecationWarning)
            return current_site

        for user in self.users:

            temp_key = token_generator.make_token(user)

            # save it to the password reset model
            # password_reset = PasswordReset(user=user, temp_key=temp_key)
            # password_reset.save()

            # send the password reset email
            path = reverse("users:account_reset_password_from_key",
                           kwargs=dict(uidb36=user_pk_to_url_str(user),
                                       key=temp_key))
            url = build_absolute_uri(
                request, path)

            context = {"site": deprecated_site,
                       "current_site": current_site,
                       "user": user,
                       "password_reset_url": url,
                       "request": request}

            if app_settings.AUTHENTICATION_METHOD \
                    != AuthenticationMethod.EMAIL:
                context['username'] = user_username(user)
            get_adapter().send_mail(
                'account/email/password_reset_key',
                email,
                context)
        return self.cleaned_data["email"]


class UserResetPasswordKeyForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super(UserResetPasswordKeyForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.TextInput(attrs={
                                                  'type': 'password',
                                                  'class': 'form-control',
                                                  'placeholder': 'New Password'})
        self.fields['password2'].widget = forms.TextInput(attrs={
                                                  'type': 'password',
                                                  'class': 'form-control',
                                                  'placeholder': 'New Password(again)'})



class UserSettingsForm(forms.ModelForm):
    def clean_remove_photo(self):
        remove = self.cleaned_data["remove_photo"]
        if remove:
            self.cleaned_data['image'] = ""

    class Meta:
        model = User
        fields = ("first_name", "last_name", "summary", "contact", "image")
        widgets = {
            'first_name': forms.TextInput(attrs={
                                    'type': 'text',
                                    'class': 'form-control',
                                    'placeholder': 'First Name'
                                    }),
            'last_name': forms.TextInput(attrs={
                                    'type': 'text',
                                    'class': 'form-control',
                                    'placeholder': 'Last Name'
                                    }),
            'summary': forms.Textarea(attrs={
                                    'class': 'form-control message',
                                    'placeholder': 'About Me'
                                    }),
            'contact': forms.TextInput(attrs={
                                    'type': 'text',
                                    'class': 'form-control',
                                    'placeholder': 'Contact Number'
                                    }),
        }


class PatientSettingsForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ("clinic", "transportation_need", "past_medications", "current_medications",
                  "height", "weight", "smoking", "alcohol", "marijuana")
        widgets = {
            'clinic': forms.Select(attrs={
                    'class': 'form-control'
                }),
        }


class DoctorSettingsForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ("specialty", "clinic", "HCAI")
        widgets = {
            'specialty': forms.Select(attrs={
                                    'class': 'form-control'
                                    }),
            'clinic': forms.Select(attrs={
                                    'class': 'form-control'
                                    }),
            'HCAI': forms.TextInput(attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'HCAI code'
                })
        }


class EmailDoctorForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                                    'type': 'email',
                                    'class': 'form-control',
                                    'placeholder': 'Enter a valid E-mail'
                                    }),
                            error_messages={
                                'invalid': "Please enter valid email address",
                                'required': "Please enter an email address"
                                })

    def send_email(self, staff_email, link):
        data = self.cleaned_data
        msg = EmailMessage('Doctor Signup Link',
                           link,
                           staff_email,
                           [data['email']])
        msg.send()

