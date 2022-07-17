from django.shortcuts import render
from .models import Customer
from django.views.generic.edit import FormView
from .forms import CustomerForm


class CustomerFormView(FormView):
    form_class = CustomerForm
    model = Customer
    template_name = 'book.html'


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')


def menu(request):
    return render(request, 'menu.html')

