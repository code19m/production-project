# Generated by Django 4.0.2 on 2022-02-19 21:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Shahar nomi')),
            ],
            options={
                'verbose_name': 'Shahar',
                'verbose_name_plural': 'Shaharlar',
            },
        ),
        migrations.CreateModel(
            name='ClientBankDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MFO', models.CharField(max_length=50)),
                ('INN', models.CharField(max_length=50)),
                ('BANK_ACCOUNT', models.CharField(max_length=50, verbose_name='Hisob raqami')),
            ],
            options={
                'verbose_name': 'Mijoz bank rekvizit',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")),
                ('time_updated', models.DateTimeField(auto_now=True, verbose_name='Yangilangan sana')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Firma nomi')),
                ('fullname', models.CharField(max_length=255, verbose_name='Direktor FIO')),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Telefon raqami mana bunday bo'lishi kerak: `998901234567`", regex='^((\\+998)|(998))\\d{9}$')], verbose_name='Telefon raqami')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Manzil')),
                ('description', models.TextField(blank=True, verbose_name='Izoh')),
                ('bank_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sales.clientbankdetail', verbose_name='Bank rekvizitlari')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.city', verbose_name='Shahar')),
            ],
            options={
                'verbose_name': 'Mijoz',
                'verbose_name_plural': 'Mijozlar',
            },
        ),
    ]