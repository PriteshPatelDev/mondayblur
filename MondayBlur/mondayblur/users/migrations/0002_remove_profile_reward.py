# Generated by Django 2.1.7 on 2019-05-08 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='reward',
        ),
    ]
