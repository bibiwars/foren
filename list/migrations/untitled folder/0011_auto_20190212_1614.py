# Generated by Django 2.1.7 on 2019-02-12 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0010_auto_20190212_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='id',
            field=models.AutoField(auto_created=True, default='X', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='case',
            name='c_id',
            field=models.IntegerField(default=0),
        ),
    ]
