# Generated by Django 3.2.12 on 2023-11-14 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gurdataApp', '0007_auto_20231113_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
