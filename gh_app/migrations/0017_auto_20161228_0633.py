# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gh_app', '0016_auto_20161228_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(default='null.jpg', upload_to='Posts/Year: %Y/Month: %m/Day: %d'),
        ),
    ]
