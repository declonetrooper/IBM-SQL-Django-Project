# Generated by Django 4.1.1 on 2022-09-22 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='isRight',
            new_name='correct',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choiceText',
        ),
        migrations.RemoveField(
            model_name='question',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='question',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='question',
            name='questionText',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='grade_point',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
