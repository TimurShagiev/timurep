# Generated by Django 4.2.5 on 2023-09-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prob_list', '0003_problem_status_alter_problem_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='actions',
            field=models.TextField(blank=True),
        ),
    ]
