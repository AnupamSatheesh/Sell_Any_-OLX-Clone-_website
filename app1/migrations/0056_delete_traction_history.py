# Generated by Django 5.1.5 on 2025-02-13 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0055_alter_traction_history_odr_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Traction_History',
        ),
    ]
