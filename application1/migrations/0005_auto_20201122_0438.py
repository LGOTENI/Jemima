# Generated by Django 3.1.3 on 2020-11-22 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0004_auto_20201122_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='nom_categorie',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='produit',
            name='quantite',
            field=models.IntegerField(),
        ),
    ]
