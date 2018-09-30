# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-21 19:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0031_auto_20180921_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='channel',
            name='rule',
        ),
        migrations.AlterField(
            model_name='image',
            name='album',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pages.Album'),
        ),
        migrations.DeleteModel(
            name='Channel',
        ),
        migrations.DeleteModel(
            name='Rule',
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='pages.Group'),
        ),
    ]
