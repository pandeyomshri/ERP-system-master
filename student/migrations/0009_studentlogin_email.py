# Generated by Django 4.0.5 on 2022-12-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_remove_studentlogin_intermediateboard_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentlogin',
            name='email',
            field=models.EmailField(default=None, editable=False, max_length=60),
        ),
    ]
