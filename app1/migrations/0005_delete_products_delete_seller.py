# Generated by Django 5.1.5 on 2025-01-23 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_products'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]
