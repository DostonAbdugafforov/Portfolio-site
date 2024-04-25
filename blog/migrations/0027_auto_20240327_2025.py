# Generated by Django 3.2.20 on 2024-03-27 15:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20240327_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='blog.blogcategory'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 15, 25, 21, 384244, tzinfo=utc), verbose_name='Nashir Sanasi'),
        ),
    ]
