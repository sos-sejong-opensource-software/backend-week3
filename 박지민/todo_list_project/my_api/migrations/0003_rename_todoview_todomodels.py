# Generated by Django 4.1.5 on 2023-01-22 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0002_rename_todo_todoview'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoView',
            new_name='TodoModels',
        ),
    ]
