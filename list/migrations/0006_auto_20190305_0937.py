# Generated by Django 2.1.7 on 2019-03-05 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_case_c_supported'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='c_supported',
            new_name='c_unsupported',
        ),
    ]
