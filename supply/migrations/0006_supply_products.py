# Generated by Django 4.2.5 on 2023-10-05 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_supplier'),
        ('supply', '0005_supply'),
    ]

    operations = [
        migrations.AddField(
            model_name='supply',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='products', to='products.product', verbose_name='Продукты'),
        ),
    ]