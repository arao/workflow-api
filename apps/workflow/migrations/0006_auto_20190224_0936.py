# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-24 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0005_auto_20190224_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='start_delta',
            field=models.DurationField(help_text='time delay between completion of parent task and star of current task'),
        ),
    ]
