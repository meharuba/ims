# Generated by Django 4.1.3 on 2023-03-22 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quotation', '0005_alter_quotation_options_remove_quotation_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
