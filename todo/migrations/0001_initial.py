# Generated by Django 3.2.10 on 2022-05-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]