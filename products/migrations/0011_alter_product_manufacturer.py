# Generated by Django 4.2.5 on 2023-10-07 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0008_supply_release_datetime'),
        ('products', '0010_alter_product_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(limit_choices_to={'node_type': 'Завод'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='supply.partner', verbose_name='Организация производитель'),
        ),
    ]
