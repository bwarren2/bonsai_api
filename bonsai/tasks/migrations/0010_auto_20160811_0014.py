# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 00:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_deck_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]