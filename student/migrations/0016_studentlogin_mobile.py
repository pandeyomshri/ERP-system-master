# Generated by Django 4.0.5 on 2023-01-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_remove_student_marks_pue_marks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentlogin',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
