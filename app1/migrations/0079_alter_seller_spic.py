# Generated by Django 5.1.5 on 2025-03-04 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0078_alter_seller_spic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='spic',
            field=models.ImageField(default='blank-profile-picture-973460_1280.webp', upload_to='images/'),
        ),
    ]
