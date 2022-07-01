# Generated by Django 3.2.13 on 2022-07-01 16:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.UUIDField(default=uuid.UUID('b0df5922-28d4-4609-9b3f-d943fadc9811'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('num_of_guests', models.IntegerField()),
                ('available_tables', models.BooleanField()),
                ('booking_duration', models.TimeField()),
                ('status_of_booking', models.BooleanField(choices=[(True, 'Booked'), (False, 'Not Booked')], default=False)),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
    ]
