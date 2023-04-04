# Generated by Django 4.1.3 on 2023-03-29 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_initial'),
        ('quotation', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotationline',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='quotationline',
            name='created_by',
        ),
        migrations.AddField(
            model_name='quotation',
            name='district',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='partner.district'),
        ),
        migrations.AlterField(
            model_name='quotationline',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='quotationline',
            name='quotation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quotation.quotation'),
        ),

    ]
