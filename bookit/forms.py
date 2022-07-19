from django import forms
from .models import Customer


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'email': ('Email Address'),
        }
        widgets = {
            'date_of_booking': DateInput(),
        }
