# Generated by Django 4.2 on 2023-04-14 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0002_counts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counts',
            name='pageVisit',
        ),
        migrations.AddField(
            model_name='counts',
            name='user',
            field=models.TextField(default=None),
        ),
    ]
