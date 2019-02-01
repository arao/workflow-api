# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-30 13:39
from __future__ import unicode_literals

import django.contrib.postgres.fields.citext
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workflow_template', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', django.contrib.postgres.fields.citext.CICharField(
                    max_length=100)),
                ('description', models.TextField()),
                ('delta_time', models.DurationField(
                    help_text='time delay between completion of parent task and star of current task')),
                ('status', models.PositiveIntegerField(choices=[
                    (1, 'ONGOING'), (2, 'COMPLETED'), (0, 'UPCOMMING')])),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                                  related_name='tasks', to=settings.AUTH_USER_MODEL)),
                ('child_task', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parents',
                    to='workflow.Task')),
                ('parent_task', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='childs',
                    to='workflow.Task')),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', django.contrib.postgres.fields.citext.CICharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('is_completed', models.BooleanField()),
                ('expected_end_time', models.DateTimeField()),
                ('creator', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('template', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='workflow_template.WorkflowTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowAccess',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.PositiveIntegerField(
                    choices=[(0, 'READ'), (1, 'READ_WRITE')])),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workflow', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='workflow.Workflow')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='workflow',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='workflow.Workflow'),
        ),
        migrations.AlterUniqueTogether(
            name='workflowaccess',
            unique_together=set([('user', 'workflow')]),
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together=set([('workflow', 'title')]),
        ),
    ]