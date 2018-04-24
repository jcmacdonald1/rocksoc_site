# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-24 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20180420_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField(blank=True, null=True)),
                ('quote', models.TextField()),
                ('info', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Quote',
            },
        ),
    ]
