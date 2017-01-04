# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gh_app', '0014_auto_20161228_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airwater_equipmentconsumable',
            name='file',
            field=models.FileField(upload_to='AirWater_EquipmentConsumables/'),
        ),
        migrations.AlterField(
            model_name='airwater_filter',
            name='file',
            field=models.FileField(upload_to='AirWater_Filters/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(default='', upload_to='Posts/Year: %Y/Month: %m/Day: %d'),
        ),
    ]