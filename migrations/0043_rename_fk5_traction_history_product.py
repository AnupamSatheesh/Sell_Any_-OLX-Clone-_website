# Generated by Django 5.1.5 on 2025-02-13 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0042_traction_history'),
    ]

    operations = [
        migrations.RenameField(
            model_name='traction_history',
            old_name='fk5',
            new_name='product',
        ),
    ]
