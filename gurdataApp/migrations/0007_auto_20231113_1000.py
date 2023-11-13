# Generated by Django 3.2.12 on 2023-11-13 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gurdataApp', '0006_systemnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergurdata',
            name='file_manager_notifications',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usergurdata',
            name='mail_notifications',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usergurdata',
            name='system_notifications',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='SystemNotification',
        ),
    ]
