# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 10:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_phase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phase',
            new_name='cur_phase',
        ),
    ]
