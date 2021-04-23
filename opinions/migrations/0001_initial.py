# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-24 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpinionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive_ops', models.IntegerField(default=1)),
                ('negative_ops', models.IntegerField(default=1)),
                ('neutral_ops', models.IntegerField(default=1)),
                ('obtain_time', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='QueryDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='opinionset',
            name='query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opinions.QueryDB'),
        ),
    ]
