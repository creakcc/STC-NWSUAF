# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-04 09:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_auto_20180704_0933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='type',
            new_name='fb_type',
        ),
    ]