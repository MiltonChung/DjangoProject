# Generated by Django 2.2.11 on 2020-07-13 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200712_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pics/wow.png', upload_to='profile_pics'),
        ),
    ]
