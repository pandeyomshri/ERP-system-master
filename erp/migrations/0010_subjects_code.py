# Generated by Django 4.0.5 on 2022-12-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0009_remove_subjects_nolr1_remove_subjects_nolr2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='code',
            field=models.CharField(default=1, max_length=6, unique=True),
            preserve_default=False,
        ),
    ]
