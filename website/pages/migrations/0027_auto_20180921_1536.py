# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-21 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0026_auto_20180920_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Event')),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='highlight',
        ),
        migrations.RemoveField(
            model_name='album',
            name='images',
        ),
        migrations.RemoveField(
            model_name='image',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
