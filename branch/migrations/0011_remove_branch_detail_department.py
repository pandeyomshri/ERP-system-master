# Generated by Django 4.0.5 on 2022-12-18 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0010_alter_branch_subjects_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch_detail',
            name='department',
        ),
    ]