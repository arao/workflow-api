# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-28 11:42
from __future__ import unicode_literals

import django.contrib.postgres.fields.citext
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField()),
                ('field_name', django.contrib.postgres.fields.citext.CICharField(max_length=254)),
                ('prev_value', models.TextField()),
                ('next_value', models.TextField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
