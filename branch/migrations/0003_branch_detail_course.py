# Generated by Django 4.0.5 on 2022-12-10 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
        ('branch', '0002_branch_subjects_subject_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch_detail',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.course'),
            preserve_default=False,
        ),
    ]
