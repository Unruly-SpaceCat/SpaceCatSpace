# Generated by Django 2.2.4 on 2019-08-29 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20190827_2340'),
        ('dashboard', '0002_auto_20190829_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallconvo',
            name='wall_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='friendmessages', to='login.User'),
        ),
    ]