# Generated by Django 5.1.5 on 2025-01-29 03:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Deleted_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.products')),
            ],
        ),
    ]
