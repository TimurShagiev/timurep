# Generated by Django 4.2.5 on 2023-10-03 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prob_list', '0005_alter_problem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='assigned_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_problems', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='problem',
            name='resolved_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resolved_problems', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='problem',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('In progress', 'In progress'), ('confirmed', 'Confirmed'), ('resolved', 'Resolved')], default='new', max_length=20),
        ),
    ]
