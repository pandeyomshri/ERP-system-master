# Generated by Django 4.0.5 on 2023-04-22 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0029_question_paper_marks_1_question_paper_marks_10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='is_lab',
            field=models.BooleanField(default=False, verbose_name='Is Lab'),
        ),
    ]
