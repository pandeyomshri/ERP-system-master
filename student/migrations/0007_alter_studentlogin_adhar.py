# Generated by Django 4.0.5 on 2022-12-19 12:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_studentlogin_intermediateboard_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlogin',
            name='adhar',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(100000000000), django.core.validators.MaxValueValidator(999999999999)], verbose_name='Adhar'),
        ),
    ]
