# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-21 14:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_auto_20180921_1536'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
    ]
