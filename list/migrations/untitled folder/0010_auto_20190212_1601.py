# Generated by Django 2.1.7 on 2019-02-12 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0009_auto_20190212_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='_id',
            new_name='c_id',
        ),
    ]
