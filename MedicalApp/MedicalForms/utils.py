from django import forms
from django.db import models


class MyCharField(models.CharField):
    def __init__(self, placeholder='', **kwargs):
        kwargs['blank'] = True
        self.placeholder = placeholder
        super(MyCharField, self).__init__(**kwargs)

    def formfield(self, **kwargs):
        defaults = {'widget': forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': self.placeholder
                }
            )}
        defaults.update(kwargs)

        return super(MyCharField, self).formfield(**defaults)


class MySelectField(models.CharField):
    def __init__(self, choices=None, **kwargs):
        kwargs['blank'] = True
        self.my_choices = None
        if choices:
            self.my_choices = (('Unknown', '----'),) + choices
        super(MySelectField, self).__init__(**kwargs)

    def formfield(self, **kwargs):
        defaults = {'widget': forms.Select(
                choices=self.my_choices,
                attrs={
                    'class': 'form-control'
                }
            )}
        defaults.update(kwargs)

        return super(MySelectField, self).formfield(**defaults)


class MyTextField(models.TextField):
    def __init__(self, placeholder='', **kwargs):
        kwargs['blank'] = True
        self.placeholder = placeholder
        super(MyTextField, self).__init__(**kwargs)

    def formfield(self, **kwargs):
        defaults = {'widget': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': self.placeholder
                }
            )}
        defaults.update(kwargs)

        return super(MyTextField, self).formfield(**defaults)


class MyNullBooleanField(models.NullBooleanField):
    def formfield(self, **kwargs):
        defaults = {'widget': forms.NullBooleanSelect(
                attrs={
                    'class': 'form-control'
                }
            )}
        defaults.update(kwargs)

        return super(MyNullBooleanField, self).formfield(**defaults)


class IntegerRangeField(models.IntegerField):
    def __init__(self, placeholder='', min_value=None, max_value=None, **kwargs):
        kwargs['null'] = True
        kwargs['blank'] = True
        self.min_value, self.max_value = min_value, max_value
        self.placeholder = placeholder
        super(IntegerRangeField, self).__init__(**kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'min_value': self.min_value,
            'max_value': self.max_value,
            'widget': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': self.placeholder
                })
        }
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)
