# Generated by Django 5.1.5 on 2025-02-13 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0050_remove_traction_history_buyer_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Traction_History',
        ),
    ]
