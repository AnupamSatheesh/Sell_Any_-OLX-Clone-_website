# Generated by Django 5.1.5 on 2025-01-31 11:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0027_buyers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyers',
            name='fk4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
