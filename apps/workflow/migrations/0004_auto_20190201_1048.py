# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-01 10:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0003_auto_20190131_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='assigne',
            new_name='assignee',
        ),
        migrations.RenameField(
            model_name='workflow',
            old_name='completed_at',
            new_name='complete_at',
        ),
        migrations.AlterField(
            model_name='task',
            name='start_delta',
            field=models.DurationField(default=datetime.timedelta(0), help_text='time delay between completion of parent task and star of current task'),
        ),
    ]
