# Generated by Django 5.1.5 on 2025-02-13 08:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0046_delete_traction_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traction_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.CharField(max_length=100)),
                ('image1', models.ImageField(upload_to='images/')),
                ('image2', models.ImageField(upload_to='images/')),
                ('image3', models.ImageField(upload_to='images/')),
                ('image4', models.ImageField(upload_to='images/')),
                ('image5', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=80)),
                ('desc', models.CharField(max_length=1000)),
                ('prize', models.IntegerField()),
                ('seller_name', models.CharField(max_length=50)),
                ('seller_age', models.IntegerField()),
                ('seller_gender', models.CharField(max_length=10)),
                ('seller_Address', models.CharField(max_length=500)),
                ('seller_email', models.EmailField(max_length=254, unique=True)),
                ('seller_number', models.IntegerField(unique=True)),
                ('buyer_name', models.CharField(max_length=50)),
                ('buyer_age', models.IntegerField()),
                ('buyer_gender', models.CharField(max_length=10)),
                ('buyer_Address', models.CharField(max_length=500)),
                ('buyer_email', models.EmailField(max_length=254, unique=True)),
                ('buyer_number', models.IntegerField(unique=True)),
                ('fk2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.seller')),
            ],
        ),
    ]
