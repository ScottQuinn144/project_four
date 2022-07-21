from django import forms
from .models import Customer


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'phone_number', 'email',
                  'num_of_guests', 'date_of_booking', 'booked_time')
        labels = {
            'email': ('Email Address'),
            'num_of_guests': ('How Many People')
        }
        widgets = {
            'date_of_booking': DateInput(),
        }
