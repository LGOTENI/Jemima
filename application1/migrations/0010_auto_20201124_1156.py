# Generated by Django 3.1.3 on 2020-11-24 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0009_auto_20201124_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='photo',
            new_name='image',
        ),
    ]