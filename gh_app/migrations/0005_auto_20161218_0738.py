# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gh_app', '0004_auto_20161218_0519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('docfile', models.FileField(upload_to='%Y/%m/%d')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
