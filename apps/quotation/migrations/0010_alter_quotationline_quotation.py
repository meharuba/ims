# Generated by Django 4.1.3 on 2023-03-29 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0009_quotationline_quotation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotationline',
            name='quotation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='quotation.quotation'),
        ),
    ]
