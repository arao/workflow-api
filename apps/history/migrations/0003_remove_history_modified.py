# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-28 18:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_history_action'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='modified',
        ),
    ]
