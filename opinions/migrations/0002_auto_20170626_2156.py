# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 16:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opinions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opinionset',
            old_name='negative_ops',
            new_name='positive_percents',
        ),
        migrations.RemoveField(
            model_name='opinionset',
            name='neutral_ops',
        ),
        migrations.RemoveField(
            model_name='opinionset',
            name='positive_ops',
        ),
    ]
