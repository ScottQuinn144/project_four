# Generated by Django 3.2.14 on 2022-07-21 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookit', '0004_auto_20220721_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='booked_time',
            field=models.CharField(choices=[('3', '9pm to close'), ('2', '7pm to 9pm'), ('1', '5pm to 7pm')], max_length=4),
        ),
        migrations.AlterField(
            model_name='customer',
            name='num_of_guests',
            field=models.CharField(choices=[('4', 4), ('1', 1), ('5', 5), ('2', 2), ('3', 3), ('6', 6)], max_length=7),
        ),
        migrations.AlterField(
            model_name='customer',
            name='table',
            field=models.CharField(choices=[(2, 'Table 3'), (4, 'Table 5'), (4, 'Table 2'), (4, 'Table 1'), (2, 'Table 6'), (4, 'Table 4'), (10, 'Table 7')], max_length=7),
        ),
    ]
