# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gh_app', '0010_auto_20161220_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='docfile1',
            field=models.FileField(default=' ', upload_to='Posts/Year: %Y/Month: %m/Day: %d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='docfile2',
            field=models.FileField(default=' ', upload_to='Posts/Year: %Y/Month: %m/Day: %d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='docfile3',
            field=models.FileField(default=' ', upload_to='Posts/Year: %Y/Month: %m/Day: %d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='docfile4',
            field=models.FileField(default=' ', upload_to='Posts/Year: %Y/Month: %m/Day: %d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='docfile5',
            field=models.FileField(default=' ', upload_to='Posts/Year: %Y/Month: %m/Day: %d'),
        ),
    ]