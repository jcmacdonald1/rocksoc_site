# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-21 22:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0036_auto_20180921_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
    ]
