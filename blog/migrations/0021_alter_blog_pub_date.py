# Generated by Django 3.2.20 on 2024-03-24 04:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_blog_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 24, 4, 37, 21, 511921, tzinfo=utc), verbose_name='Nashir Sanasi'),
        ),
    ]
