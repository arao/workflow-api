# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-31 07:45
from __future__ import unicode_literals

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_id',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, unique=True, verbose_name='task id'),
        ),
        migrations.AddField(
            model_name='workflow',
            name='workflow_id',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, unique=True, verbose_name='workflow id'),
        ),
    ]