# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20160809_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='enable_keyboard_shortcuts',
            field=models.BooleanField(default=False),
        ),
    ]
