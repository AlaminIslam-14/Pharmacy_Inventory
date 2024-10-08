# Generated by Django 5.0.6 on 2024-08-19 09:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0003_alter_drug_name'),
        ('stock', '0002_remove_stock_batch_id_alter_stock_drug_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='drug_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='drug.drug'),
        ),
    ]
