from .models import Employee
from django import forms
from django.forms import ModelForm, Textarea
from django.core.exceptions import ValidationError

from django.utils.translation import ugettext_lazy as _

class AddEmployee(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def clean_first_name(self):
        data = self.cleaned_data['first_name']

        # Check if first_name is letters only
        if not all(x.isalpha() for x in data):
            raise ValidationError(_('Only alphabetical letters are allowed'))

        # Remember to always return the cleaned data.
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']

        # Check if last_name is letters only
        if not all(x.isalpha() for x in data):
            raise ValidationError(_('Only alphabetical letters are allowed'))

        # Remember to always return the cleaned data.
        return data