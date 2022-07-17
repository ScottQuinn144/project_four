from django import forms
from .models import Customer


class CustomerForm(forms.Form):
    model = Customer
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
