# Generated by Django 4.0.5 on 2023-03-28 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0026_question_paper_ques13_question_paper_ques14_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question_paper',
            name='Ques1',
        ),
        migrations.RemoveField(
            model_name='question_paper',
            name='Ques10',
        ),
        migrations.RemoveField(
            model_name='question_paper',
            name='Ques11',
        ),
        migrations.RemoveField(
            model_name='question_paper',
            name='Ques12',
        ),
        migrations.RemoveField(
            model_name='question_paper',
            name='Ques13',
        ),
        migrations.RemoveField(
            model_name='question_paper',
            name='Ques14',
        ),
        migrations.RemoveField(
            model_name='question_paper',
            name='Ques15',
        ),
        migrations.RemoveField(
            model_name='question_paper',
            name='Ques2',
        ),
        migrations.RemoveField(
            model_name='question_paper',
            name='Ques3',
        ),
        migrations.RemoveField(
            model_name='question_paper',
            name='Ques4',
        ),
        migrations.RemoveField(
            model_name='question_paper',
            name='Ques5',
        ),
        migrations.RemoveField(
            model_name='question_paper',
            name='Ques6',
        ),
        migrations.RemoveField(
            model_name='question_paper',
            name='Ques7',
        ),
        migrations.RemoveField(
            model_name='question_paper',
            name='Ques8',
        ),
        migrations.RemoveField(
            model_name='question_paper',
            name='Ques9',
        ),
        migrations.AddField(
            model_name='question',
            name='paper',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.question_paper'),
            preserve_default=False,
        ),
    ]