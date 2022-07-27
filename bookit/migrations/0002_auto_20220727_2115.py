# Generated by Django 3.2.14 on 2022-07-27 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='booked_time',
            field=models.CharField(choices=[('21-23', '9pm to close'), ('19-21', '7pm to 9pm'), ('17-10', '5pm to 7pm')], max_length=12),
        ),
        migrations.AlterField(
            model_name='customer',
            name='num_of_guests',
            field=models.CharField(choices=[('1', 1), ('6', 6), ('2', 2), ('4', 4), ('3', 3), ('5', 5)], max_length=7),
        ),
        migrations.AlterField(
            model_name='customer',
            name='table',
            field=models.CharField(choices=[(2, 'Table 6'), (4, 'Table 5'), (2, 'Table 3'), (4, 'Table 4'), (4, 'Table 1'), (10, 'Table 7'), (4, 'Table 2')], max_length=7),
        ),
    ]