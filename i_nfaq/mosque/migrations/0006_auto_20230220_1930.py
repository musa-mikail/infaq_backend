# Generated by Django 3.1 on 2023-02-20 18:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosque', '0005_auto_20230220_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mosque',
            name='mosque_phone',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex='^\x01?\\d{9,10}$')]),
        ),
    ]