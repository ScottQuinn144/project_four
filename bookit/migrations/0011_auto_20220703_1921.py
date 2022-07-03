# Generated by Django 3.2.13 on 2022-07-03 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookit', '0010_alter_customer_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='customer',
        ),
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to='bookit.customer'),
        ),
    ]