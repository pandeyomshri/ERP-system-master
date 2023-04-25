# Generated by Django 4.0.5 on 2022-12-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_studentlogin_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentlogin',
            name='email',
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='personalEmail',
            field=models.EmailField(default='abhinavsinghal256@gmail.com', max_length=30),
            preserve_default=False,
        ),
    ]