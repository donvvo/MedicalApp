from django import forms

from allauth.account.forms import SignupForm

from .models import Clinic


class ClinicUserSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(ClinicUserSignupForm, self).__init__(*args, **kwargs)
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


class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ('name', 'phone', 'description', 'city', 'address', 'postal_code',
        'start_time_mon', 'end_time_mon', 'start_time_tue', 'end_time_tue',
        'start_time_wed', 'end_time_wed', 'start_time_thurs', 'end_time_thurs',
        'start_time_fri', 'end_time_fri', 'start_time_sat', 'end_time_sat',
        'start_time_sun', 'end_time_sun')