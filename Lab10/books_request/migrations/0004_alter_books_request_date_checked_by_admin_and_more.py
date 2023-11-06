# Generated by Django 4.2.7 on 2023-11-06 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_request', '0003_books_request_date_checked_by_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books_request',
            name='date_checked_by_admin',
            field=models.DateTimeField(default=datetime.datetime(1000, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='books_request',
            name='date_withdrawal',
            field=models.DateTimeField(default=datetime.datetime(1000, 1, 1, 0, 0)),
        ),
    ]