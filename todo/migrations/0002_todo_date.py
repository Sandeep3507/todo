# Generated by Django 2.1.5 on 2019-02-18 11:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
