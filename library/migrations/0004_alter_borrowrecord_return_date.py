# Generated by Django 4.2.11 on 2024-04-27 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_borrowrecord_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowrecord',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 27, 17, 44, 52, 74666, tzinfo=datetime.timezone.utc)),
        ),
    ]
