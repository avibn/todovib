# Generated by Django 3.2.4 on 2021-06-25 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_added_lists'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitem',
            name='completed',
            field=models.BooleanField(default=False, help_text='The completion status of the task.'),
        ),
    ]