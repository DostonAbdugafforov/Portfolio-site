# Generated by Django 3.2.20 on 2024-03-27 15:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20240327_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 15, 16, 44, 959008, tzinfo=utc), verbose_name='Nashir Sanasi'),
        ),
    ]
