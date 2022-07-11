from django.shortcuts import render
from .models import Customer
from django.views import generic


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')


def menu(request):
    return render(request, 'menu.html')


class CustomerForm(generic.ListView):
    model = Customer
    template_name = "book.html"
    paginate_by = 2

