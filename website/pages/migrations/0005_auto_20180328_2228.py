# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-28 21:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20180328_2044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='published_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='created_date',
        ),
    ]
