# Generated by Django 3.2.20 on 2024-03-17 12:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20240317_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 17, 12, 30, 57, 739253, tzinfo=utc), verbose_name='Nashir Sanasi'),
        ),
    ]
