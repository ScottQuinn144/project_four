from django.shortcuts import render, redirect
from .forms import CustomerForm
from django.conf import settings
from django.core.mail import send_mail


def MakeABooking(response):
    if response.method == "POST":
        form = CustomerForm(response.POST)
        if form.is_valid():
            username = response.POST['first_name']
            email = response.POST['email']
            phone = response.POST['phone_number']
            guests = response.POST['num_of_guests']
            date = response.POST['date_of_booking']
            time = response.POST['booked_time']

        subject = 'Thank You For Your Booking'
        message = f'Hello {username}, you have booked on {date} at {time} for {guests} number of peeople. We have {phone} and {email} as your contact details.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

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
