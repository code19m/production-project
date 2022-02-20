# Generated by Django 4.0.2 on 2022-02-20 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('storage', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveinvoice',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to=settings.AUTH_USER_MODEL, verbose_name='Hodim'),
        ),
        migrations.AddField(
            model_name='leaveinvoice',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.storage', verbose_name='Ombor'),
        ),
        migrations.AddField(
            model_name='defectiveproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defective_products', to='storage.product', verbose_name='Mahsulot nomi'),
        ),
    ]
