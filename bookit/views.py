from django.shortcuts import render, redirect
from .forms import CustomerForm
from . import models


def MakeABooking(response):
    Customer = models.Customer
    if response.method == "POST":
        form = CustomerForm(response.POST)
        if Customer.num_of_guests == models.TABLES:
            
            form.is_valid()
            form.save()
        else:
            ValueError('Please Contact Us on: 1234 5678 90')
            form = CustomerForm(response.POST)
        form.save()
        return redirect('home')
    else:
        form = CustomerForm()
    return render(response, 'book.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')


def menu(request):
    return render(request, 'menu.html')
