# Generated by Django 3.2.14 on 2022-07-17 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookit', '0013_auto_20220703_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='available_tables',
        ),
    ]