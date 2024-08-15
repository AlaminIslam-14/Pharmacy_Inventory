# Generated by Django 5.0.6 on 2024-08-15 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('company', 'Seller'), ('pharmacy', 'Buyer')], max_length=50)),
                ('acc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.accounts')),
            ],
        ),
    ]
