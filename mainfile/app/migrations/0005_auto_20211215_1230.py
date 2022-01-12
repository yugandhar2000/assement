# Generated by Django 3.2.9 on 2021-12-15 07:00

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211214_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Customer1',
        ),
    ]