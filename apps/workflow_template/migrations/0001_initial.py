# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-18 10:56
from __future__ import unicode_literals

import apps.workflow_template.models
import django.contrib.postgres.fields.citext
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkflowTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', django.contrib.postgres.fields.citext.CICharField(max_length=100, unique=True)),
                ('structure', django.contrib.postgres.fields.jsonb.JSONField()),
                ('logo', models.ImageField(blank=True, help_text='Template logo picture', upload_to=apps.workflow_template.models.logo_dir)),
            ],
        ),
    ]
