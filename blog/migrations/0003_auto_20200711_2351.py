# Generated by Django 2.2.11 on 2020-07-12 06:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200711_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 12, 6, 51, 46, 600695, tzinfo=utc)),
        ),
    ]
