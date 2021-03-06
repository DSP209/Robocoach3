# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-25 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='foot',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='photo',
            name='hands',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
