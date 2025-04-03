# Generated by Django 5.1.5 on 2025-01-31 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_delete_buyers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('number', models.IntegerField(unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50, unique=True)),
                ('fk4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.products')),
            ],
        ),
    ]
