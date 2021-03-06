# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 14:05
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirWater_EquipmentConsumable',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('file', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AirWater_Filter',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('file', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('image_file', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('video_file', cloudinary.models.CloudinaryField(max_length=255, verbose_name='video')),
                ('video_exists', models.BooleanField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
