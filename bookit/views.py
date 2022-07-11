from django.shortcuts import render
from django.views import View


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def book(request):
    return render(request, 'book.html')


def gallery(request):
    return render(request, 'gallery.html')


def menu(request):
    return render(request, 'menu.html')
