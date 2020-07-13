# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-02 22:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_auto_20190202_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='c_date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='case',
            name='c_status',
            field=models.BooleanField(default=False),
        ),
    ]
