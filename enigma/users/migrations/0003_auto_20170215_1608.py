# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170215_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cur_phase',
            field=models.IntegerField(default=1, null=True, verbose_name='Current phase'),
        ),
    ]
