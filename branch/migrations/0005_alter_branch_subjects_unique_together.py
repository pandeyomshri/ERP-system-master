# Generated by Django 4.0.5 on 2022-12-10 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
        ('teacher', '0001_initial'),
        ('branch', '0004_branch_detail_section'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='branch_subjects',
            unique_together={('branch_subject', 'subject_teacher')},
        ),
    ]
