# Generated by Django 2.2.4 on 2019-08-26 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=65)),
                ('user_level', models.CharField(default='generic', max_length=10)),
                ('avatar', models.IntegerField(default='13')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
