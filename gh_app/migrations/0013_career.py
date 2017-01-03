# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gh_app', '0012_auto_20161228_0440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
