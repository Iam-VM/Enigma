# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 12:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20170301_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2017, 3, 1, 12, 53, 42, 222241, tzinfo=utc)),
        ),
    ]
