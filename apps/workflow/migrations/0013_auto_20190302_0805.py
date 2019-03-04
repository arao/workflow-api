# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-02 08:05
from __future__ import unicode_literals

from django.db import migrations
import partial_index


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0012_workflowaccess_is_active'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='workflowaccess',
            unique_together=set([]),
        ),
        migrations.AddIndex(
            model_name='workflowaccess',
            index=partial_index.PartialIndex(fields=['employee', 'workflow'], name='workflow_wo_employe_f52ffe_partial', unique=True, where=partial_index.PQ(is_active=True)),
        ),
    ]