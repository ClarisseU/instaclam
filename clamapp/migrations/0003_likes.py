# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-20 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clamapp', '0002_auto_20191020_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postid', models.ImageField(upload_to='')),
                ('like', models.CharField(max_length=20)),
            ],
        ),
    ]
