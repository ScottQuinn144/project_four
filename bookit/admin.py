from django.contrib import admin
from .models import Customer, Booking


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email')
    search_fields = ['phone_number', 'email']
    list_filter = ('email', 'phone_number')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('num_of_guests', 'which_tables', 'booked_time')
    search_fields = ['customer', 'booked_time']
    list_filter = ('date_of_booking', 'customer')
