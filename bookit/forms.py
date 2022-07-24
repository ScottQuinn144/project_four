from django import forms
from .models import Customer


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'phone_number', 'email',
                  'num_of_guests', 'date_of_booking', 'booked_time',
                  'other_info')
        labels = {
            'email': ('Email Address'),
            'num_of_guests': ('How Many People'),
            'other_info': ('Special Requirements?')
        }
        widgets = {
            'date_of_booking': DateInput(),
            'other_info': forms.Textarea(attrs={'rows': 6})
        }
        errors = 'Please Contact The Restaurant To Book'


class EmailForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
