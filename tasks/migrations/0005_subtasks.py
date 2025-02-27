# Generated by Django 5.1.6 on 2025-02-25 12:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_member_color_member_phone_alter_task_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subtasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('state', models.BooleanField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='tasks.task')),
            ],
        ),
    ]
