# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-04 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_auto_20190202_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='c_file',
            field=models.FileField(upload_to=b'uploads/'),
        ),
    ]
