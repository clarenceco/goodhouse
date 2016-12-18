# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gh_app', '0005_auto_20161218_0738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category1_Product',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('docfile', models.FileField(upload_to='Category1_Products/')),
            ],
        ),
        migrations.CreateModel(
            name='Category2_Product',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('docfile', models.FileField(upload_to='Category2_Products/')),
            ],
        ),
        migrations.CreateModel(
            name='Category3_Product',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('docfile', models.FileField(upload_to='Category3_Products/')),
            ],
        ),
        migrations.CreateModel(
            name='Category4_Product',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('docfile', models.FileField(upload_to='Category4_Products/')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='docfile',
            field=models.FileField(upload_to='Posts/Year: %Y/Month: %m/Day: %d'),
        ),
    ]
