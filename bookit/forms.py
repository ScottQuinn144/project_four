from django import forms
from .models import Customer, Booking


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date_of_booking', 'booked_time', 'num_of_guests']
