from django.db import models

TIMES = {
    ('17-10', '5pm to 7pm'),
    ('19-21', '7pm to 9pm'),
    ('21-23', '9pm to close')
}


GUESTS = {
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
    ('6', 6),
}

TABLES = {
    (4, 'Table 1'),
    (4, 'Table 2'),
    (2, 'Table 3'),
    (4, 'Table 4'),
    (4, 'Table 5'),
    (2, 'Table 6'),
    (10, 'Table 7'),
}

MAX_CAP = 30


class Customer(models.Model):
    '''
    Model for the customer including all information that will be required to
    take the booking
    '''
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15, primary_key=True)
    email = models.EmailField(max_length=50)
    date_of_booking = models.DateField()
    booked_time = models.CharField(max_length=50, choices=TIMES)
    num_of_guests = models.CharField(max_length=50, choices=GUESTS)
    table = models.CharField(max_length=50, choices=TABLES)
    other_info = models.TextField(max_length=200, default='')

    class Meta:
        '''
        Order the customers by first name in accending order
        '''
        ordering = ["last_name"]

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
