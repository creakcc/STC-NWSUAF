# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-27 07:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20180627_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='file',
            field=models.ForeignKey(blank=True, default=111, on_delete=django.db.models.deletion.CASCADE, to='share.File'),
            preserve_default=False,
        ),
    ]