# Generated by Django 4.0.5 on 2023-01-18 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_remove_teacherlogin_department_teacherlogin_branch_and_more'),
        ('attendance', '0007_alter_mark_attendance_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark_attendance',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacherlogin'),
            preserve_default=False,
        ),
    ]
