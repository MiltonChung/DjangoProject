# Generated by Django 2.2.13 on 2020-07-15 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200712_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank='True', default='', help_text='Enter your bio here'),
        ),
    ]
