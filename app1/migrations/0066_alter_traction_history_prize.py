# Generated by Django 5.1.5 on 2025-02-16 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0065_alter_products_desc_alter_products_prize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traction_history',
            name='prize',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
