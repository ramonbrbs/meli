# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meli_account', '0002_auto_20170130_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='meliaccount',
            name='expires',
            field=models.BigIntegerField(default=666),
            preserve_default=False,
        ),
    ]
