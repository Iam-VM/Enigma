# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 17:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0012_auto_20170304_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='title',
        ),
    ]
