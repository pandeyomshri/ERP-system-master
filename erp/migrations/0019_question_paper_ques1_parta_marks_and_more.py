# Generated by Django 4.0.5 on 2023-01-25 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0018_question_paper'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_paper',
            name='Ques1_partA_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques1_partB_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques1_partC_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques1_partD_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques1_partE_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques1_partF_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques1_partG_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques1_partH_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques1_partI_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques1_partJ_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques2_partA_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques2_partB_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques2_partC_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques2_partD_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques2_partE_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques3_partA_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques3_partB_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques4_partA_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques4_partB_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques5_partA_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques5_partB_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques6_partA_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques6_partB_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques7_partA_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='Ques7_partB_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_paper',
            name='total_marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subjects',
            name='code',
            field=models.CharField(max_length=7, unique=True),
        ),
    ]
