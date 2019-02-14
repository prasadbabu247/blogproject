# Generated by Django 2.1.5 on 2019-02-11 14:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20190211_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 11, 14, 29, 44, 580710, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 11, 14, 29, 44, 580710, tzinfo=utc)),
        ),
    ]