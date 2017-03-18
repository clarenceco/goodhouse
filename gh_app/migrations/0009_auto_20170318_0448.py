# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-18 04:48
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gh_app', '0008_featured_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Water_Filter',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('file', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='AirWater_Filter',
            new_name='Air_Filter',
        ),
        migrations.RenameModel(
            old_name='AirWater_EquipmentConsumable',
            new_name='Dust_Filter',
        ),
    ]