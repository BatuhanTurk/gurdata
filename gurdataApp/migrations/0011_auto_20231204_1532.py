# Generated by Django 3.2.12 on 2023-12-04 15:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gurdataApp', '0010_auto_20231204_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='datadownloadgurdata',
            name='data_active',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datagurdata',
            name='data_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
