# Generated by Django 2.1.5 on 2019-02-12 11:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20190211_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 11, 21, 56, 959653, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 11, 21, 56, 959653, tzinfo=utc)),
        ),
    ]