# Generated by Django 2.2.4 on 2019-08-28 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kithub', '0003_auto_20190828_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hubcomment',
            name='hubconvo_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hubcomments', to='kithub.Hubconvo'),
        ),
        migrations.AlterField(
            model_name='hubreply',
            name='hubcomment_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hubreplies', to='kithub.Hubconvo'),
        ),
    ]
