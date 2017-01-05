# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 15:17
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gh_app', '0006_auto_20170105_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_file',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
