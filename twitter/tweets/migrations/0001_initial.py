# Generated by Django 2.0.5 on 2019-02-21 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=1000)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2019, 2, 21, 17, 27, 30, 687774))),
            ],
        ),
    ]