# Generated by Django 4.2 on 2024-07-28 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_lessonprogress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='module',
        ),
        migrations.DeleteModel(
            name='Module',
        ),
    ]
