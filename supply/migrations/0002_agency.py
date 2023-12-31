# Generated by Django 4.2.5 on 2023-10-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('country', models.CharField(max_length=55, verbose_name='Страна')),
                ('city', models.CharField(max_length=55, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=20, verbose_name='Номер дома')),
                ('node_type', models.CharField(choices=[('Завод', 'Завод'), ('Розничная сеть', 'Розничная сеть'), ('ИП', 'ИП')], max_length=255, verbose_name='Тип звена')),
                ('is_active', models.BooleanField(default=True, verbose_name='Актив организации')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
    ]
