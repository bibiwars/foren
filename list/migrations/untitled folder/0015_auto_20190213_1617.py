# Generated by Django 2.1.7 on 2019-02-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0014_remove_case_c_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='id',
        ),
        migrations.AddField(
            model_name='case',
            name='c_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
