# Generated by Django 3.1.3 on 2020-11-27 13:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0012_auto_20201127_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='date_creation',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 27, 13, 18, 37, 674940, tzinfo=utc), verbose_name='Date création'),
        ),
    ]
