from django.shortcuts import render, redirect
from .forms import CustomerForm, EmailForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def MakeABooking(response):
    if response.method == "POST":
        form = CustomerForm(response.POST)
        form.is_valid()
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


def ContactView(request):
    if request.method == 'GET':
        form = EmailForm()
    else:
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('book')
    return render(request, "contact.html", {'form': form})
