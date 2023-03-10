# Generated by Django 4.1.3 on 2023-03-10 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('partner', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogue', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionline',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transactionline',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.product'),
        ),
        migrations.AddField(
            model_name='transactionline',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.transaction'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction',
            name='dealer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.dealer'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.supplier'),
        ),
    ]
