# Generated by Django 4.2.1 on 2023-11-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petmatch', '0005_pet_latitude_pet_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='latitude',
            field=models.FloatField(default=-46.6349803, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='longitude',
            field=models.FloatField(default=-23.5514953, verbose_name='Longitude'),
        ),
    ]
