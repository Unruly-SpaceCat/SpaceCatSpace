# Generated by Django 2.2.4 on 2019-08-27 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20190827_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friend',
            field=models.ManyToManyField(related_name='_user_friend_+', to='login.User'),
        ),
    ]