# Generated by Django 3.1.3 on 2020-11-22 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0005_auto_20201122_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.FileField(upload_to='img'),
        ),
    ]
