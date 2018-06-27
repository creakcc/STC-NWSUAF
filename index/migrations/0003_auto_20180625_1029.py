# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-25 10:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20180625_0801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('desc', models.TextField()),
            ],
            options={
                'verbose_name': '学院',
                'verbose_name_plural': '学院',
            },
        ),
        migrations.CreateModel(
            name='Collegetype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('desc', models.TextField()),
            ],
            options={
                'verbose_name': '学院类型',
                'verbose_name_plural': '学院类型',
            },
        ),
        migrations.AddField(
            model_name='colleges',
            name='classify',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Collegetype'),
        ),
    ]
