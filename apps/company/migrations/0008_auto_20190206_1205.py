# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-06 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20190201_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercompany',
            name='join_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usercompany',
            name='left_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
