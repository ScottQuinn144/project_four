import uuid
from django.db import models
from django.contrib.auth.models import User


STATUS = ((True, "Booked"), (False, "Not Booked"))


class Customer(models.Model):
    '''
    Model for the customer including all information that will be required to take the booking
    '''
    customer_id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4(), editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    full_name = [(first_name, 'First Name'), (last_name, 'Last Name')]
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=50)
    num_of_guests = models.IntegerField(editable=True)
    available_tables = models.BooleanField()
    booking_duration = models.TimeField()
    status_of_booking = models.BooleanField(choices=STATUS, default=False)

    class Meta:
        '''
        Order the customers by first name in accending order
        '''
        ordering = ["first_name"]

    def __str__(self):
        return f"This table was booked by: {self.full_name}"
