# Generated by Django 4.2 on 2023-04-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pageVisit', models.IntegerField(default=0)),
            ],
        ),
    ]
