# Generated by Django 3.2.10 on 2022-05-14 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_no',
        ),
    ]