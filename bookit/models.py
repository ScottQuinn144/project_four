from django.db import models


STATUS = ((1, "Booked"), (0, "Not Booked"))
AVAILABLE = ((1, 'Yes'), (0, 'No'))


class Customer(models.Model):
    '''
    Model for the customer including all information that will be required to take the booking
    '''
    customer_id = models.IntegerField(unique=True, primary_key=True, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
   

    class Meta:
        '''
        Order the customers by first name in accending order
        '''
        ordering = ["last_name"]

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Booking(models.Model):
    '''
    Information for making a booking
    '''
    customer = models.ManyToManyField(Customer)
    date_of_booking = models.DateField()
    booked_time = models.CharField(max_length=15)
    num_of_guests = models.IntegerField()
    available_seats = 30
    status_of_booking = models.BooleanField(choices=STATUS, default=False)
    which_tables = models.CharField(max_length=10)

    class Meta:
        '''
        Order of booked tables by time in accending order
        '''
        ordering = ["booked_time"]

    def __str__(self):
        return f"BOOKING: Table: {self.which_tables}| Time: {self.booked_time}| Guests: {self.num_of_guests}"
