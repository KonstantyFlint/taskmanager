# Generated by Django 4.1.7 on 2023-03-05 21:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskmanager', '0003_historicaltaskmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricalTaskModel',
            new_name='HistoricalTask',
        ),
        migrations.RenameModel(
            old_name='TaskModel',
            new_name='Task',
        ),
        migrations.AlterModelOptions(
            name='historicaltask',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical task', 'verbose_name_plural': 'historical tasks'},
        ),
    ]
