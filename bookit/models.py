from django.db import models

TIMES = (
    ('1', '5pm to 7pm'),
    ('2', '7pm to 9pm'),
    ('3', '9pm to close'),
)


GUESTS = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
    ('6', 6),
)


class Customer(models.Model):
    '''
    Model for the customer including all information that will be required to take the booking
    '''
    customer_id = models.IntegerField(unique=True, primary_key=True, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    date_of_booking = models.DateTimeField()
    booked_time = models.CharField(max_length=4, choices=TIMES, default='5pm-7pm')
    num_of_guests = models.CharField(max_length=7, choices=GUESTS, default='1')

    class Meta:
        '''
        Order the customers by first name in accending order
        '''
        ordering = ["last_name"]

    def __str__(self):
        return f"{self.last_name}, {self.first_name} booked for {self.num_of_guests} on {self.date_of_booking}"
