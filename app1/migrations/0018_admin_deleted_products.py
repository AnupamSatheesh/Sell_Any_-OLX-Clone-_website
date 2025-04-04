# Generated by Django 5.1.5 on 2025-01-29 04:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_delete_admin_deleted_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Deleted_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=1000)),
                ('prize', models.IntegerField()),
                ('fk3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.seller')),
            ],
        ),
    ]
