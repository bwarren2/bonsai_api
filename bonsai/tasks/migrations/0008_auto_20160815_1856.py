# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20160809_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]