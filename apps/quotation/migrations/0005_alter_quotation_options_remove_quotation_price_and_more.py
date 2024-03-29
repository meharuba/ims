# Generated by Django 4.1.3 on 2023-03-22 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogue', '0002_initial'),
        ('quotation', '0004_alter_quotation_options_quotation_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quotation',
            options={},
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='price',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='product',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='quantity',
        ),
        migrations.CreateModel(
            name='QuotationLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.product')),
                ('quotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotation.quotation')),
            ],
        ),
    ]
