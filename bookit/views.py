from django.shortcuts import render, redirect
from .forms import CustomerForm


def MakeABooking(response):
    if response.method == "POST":
        form = CustomerForm(response.POST)
        guests = 6
        if form.is_valid():
            if guests > 6:
                form = CustomerForm()
            return render(response, 'book.html', {'form': form})
        else:
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
