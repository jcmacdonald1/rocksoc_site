# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-24 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
