# Generated by Django 2.2.4 on 2019-08-28 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20190827_2340'),
        ('kithub', '0005_auto_20190828_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hubconvo',
            name='likes',
        ),
        migrations.AddField(
            model_name='hubconvo',
            name='like',
            field=models.ManyToManyField(null=True, related_name='hubconvolikes', to='login.User'),
        ),
    ]
