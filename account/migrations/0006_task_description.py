# Generated by Django 5.1.4 on 2024-12-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_task_creator_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default='Default task'),
        ),
    ]
