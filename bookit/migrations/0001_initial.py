# Generated by Django 3.2.14 on 2022-07-27 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50)),
                ('date_of_booking', models.DateField()),
                ('booked_time', models.CharField(choices=[('19-21', '7pm to 9pm'), ('21-23', '9pm to close'), ('17-10', '5pm to 7pm')], max_length=12)),
                ('num_of_guests', models.CharField(choices=[('1', 1), ('5', 5), ('2', 2), ('4', 4), ('3', 3), ('6', 6)], max_length=7)),
                ('table', models.CharField(choices=[(4, 'Table 1'), (2, 'Table 3'), (4, 'Table 2'), (10, 'Table 7'), (2, 'Table 6'), (4, 'Table 5'), (4, 'Table 4')], max_length=7)),
                ('other_info', models.TextField(default='', max_length=200)),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
    ]
