# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gh_app', '0005_auto_20170104_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='video_file',
            new_name='video_URL',
        ),
        migrations.AddField(
            model_name='post',
            name='image_exists',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]