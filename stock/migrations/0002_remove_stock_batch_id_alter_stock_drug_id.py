# Generated by Django 5.0.6 on 2024-08-19 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0003_alter_drug_name'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='batch_id',
        ),
        migrations.AlterField(
            model_name='stock',
            name='drug_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drug.drug', unique=True),
        ),
    ]
