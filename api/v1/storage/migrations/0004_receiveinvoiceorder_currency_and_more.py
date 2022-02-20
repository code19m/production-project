# Generated by Django 4.0.2 on 2022-02-20 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_cashbox_cashier'),
        ('storage', '0003_leaveinvoiceorder_receiveinvoiceorder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiveinvoiceorder',
            name='currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='finance.currency', verbose_name='Valyuta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receiveinvoiceorder',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Narxi'),
            preserve_default=False,
        ),
    ]