from django.shortcuts import render, redirect
from .forms import CustomerForm, BookingForm


def MakeABooking(response):
    if response.method == "POST":
        form = CustomerForm(response.POST)
        form.is_valid()
        form.save()
        return redirect('booking')
    else:
        form = CustomerForm()
    return render(response, 'book.html', {'form': form})


def MakeABook(response):
    if response.method == "POST":
        form = BookingForm(response.POST)
        form.is_valid()
        form.save()
        return redirect('home')
    else:
        form = BookingForm()
    return render(response, 'booking.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')


def menu(request):
    return render(request, 'menu.html')
