# Generated by Django 3.2.13 on 2022-07-03 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookit', '0009_alter_booking_booked_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['last_name']},
        ),
    ]