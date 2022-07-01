# Generated by Django 3.2.13 on 2022-07-01 16:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bookit', '0002_alter_customer_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.UUIDField(default=uuid.UUID('a424266d-07b0-487f-8349-f5082766a448'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
