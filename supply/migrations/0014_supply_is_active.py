# Generated by Django 4.2.5 on 2023-10-07 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0013_remove_supply_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='supply',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активность заявки'),
        ),
    ]
