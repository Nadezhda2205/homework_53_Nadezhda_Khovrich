# Generated by Django 4.1.1 on 2022-09-22 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_rename_description_task_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='header',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание'),
        ),
    ]
