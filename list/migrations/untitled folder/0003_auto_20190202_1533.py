# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-02 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_auto_20190202_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='c_type',
            field=models.CharField(choices=[(b'memory', b'memory'), (b'disk', b'disk'), (b'network', b'network'), (b'log', b'log')], default=b'memory', max_length=250),
        ),
    ]
