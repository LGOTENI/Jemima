# Generated by Django 3.1.3 on 2020-11-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0008_auto_20201124_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='photo',
            field=models.FileField(upload_to='img'),
        ),
    ]