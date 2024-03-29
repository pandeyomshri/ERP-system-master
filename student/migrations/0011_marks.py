# Generated by Django 4.0.5 on 2022-12-30 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0017_alter_subjects_to1_alter_subjects_to2_and_more'),
        ('student', '0010_remove_studentlogin_email_studentlogin_personalemail'),
    ]

    operations = [
        migrations.CreateModel(
            name='marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment1_marks', models.IntegerField(blank=True, null=True)),
                ('assignment2_marks', models.IntegerField(blank=True, null=True)),
                ('assignment3_marks', models.IntegerField(blank=True, null=True)),
                ('assignment4_marks', models.IntegerField(blank=True, null=True)),
                ('assignment5_marks', models.IntegerField(blank=True, null=True)),
                ('st1_marks', models.IntegerField(blank=True, null=True)),
                ('st2_marks', models.IntegerField(blank=True, null=True)),
                ('pue_marks', models.IntegerField(blank=True, null=True)),
                ('re_pue_marks', models.IntegerField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentlogin')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.subjects')),
            ],
        ),
    ]
