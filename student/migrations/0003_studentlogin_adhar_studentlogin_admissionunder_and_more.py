# Generated by Django 4.0.5 on 2022-12-19 10:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_studentlogin_isactive_studentlogin_doa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentlogin',
            name='adhar',
            field=models.IntegerField(default=123456789123, max_length=12, verbose_name=django.core.validators.MinLengthValidator(12)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='admissionUnder',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='bloodGroup',
            field=models.CharField(default=1, help_text='In Format A+', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='currAddress',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='fatherEmail',
            field=models.EmailField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='fatherIncome',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='fatherMobile',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='fatherName',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='fatherProfession',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='highSchoolBoard',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='highSchoolName',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='highSchoolRollNo',
            field=models.IntegerField(default=1, max_length=12, verbose_name='10th Roll Number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='maritalStatus',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='mobile',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='motherEmail',
            field=models.EmailField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='motherIncome',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='motherMobile',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='motherName',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='motherProfession',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='permanentAddress',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='personalEmail',
            field=models.EmailField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='status',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentlogin',
            name='sub_status',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentlogin',
            name='email',
            field=models.EmailField(default=None, editable=False, max_length=60),
        ),
    ]