# Generated by Django 3.2.12 on 2024-01-20 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gurdataApp', '0017_rename_genre_datacategorygurdata_category_svg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datacategorygurdata',
            name='category_svg',
            field=models.CharField(choices=[(1, 'Demografi'), (2, 'Araç'), (3, 'Finans'), (4, 'Trafik'), (5, 'Hava')], default='R', max_length=2),
        ),
    ]
