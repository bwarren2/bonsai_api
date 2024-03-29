# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_user_show_help'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='show_help_brainstorm',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='show_help_execute',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='show_help_plan',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='show_help_refine',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='show_help_review',
            field=models.BooleanField(default=True),
        ),
    ]
