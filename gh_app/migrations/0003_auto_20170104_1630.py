# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 16:30
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gh_app', '0002_auto_20170104_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video_file',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]