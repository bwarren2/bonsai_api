# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_merge_20160815_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='show_help',
            field=models.BooleanField(default=True),
        ),
    ]
