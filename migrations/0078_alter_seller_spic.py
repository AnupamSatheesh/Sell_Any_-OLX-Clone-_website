# Generated by Django 5.1.5 on 2025-03-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0077_alter_seller_spic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='spic',
            field=models.ImageField(default='default.webp', upload_to='images/'),
        ),
    ]
