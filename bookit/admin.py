from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'date_of_booking', 'booked_time', 'table')
    search_fields = ['phone_number', 'email']
    list_filter = ('email', 'phone_number')
