# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-28 13:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('share', '0001_initial'),
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('content', models.ImageField(blank=True, default='', upload_to='static/upload/evidence')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User')),
            ],
            options={
                'verbose_name': '证据',
                'verbose_name_plural': '证据',
                'ordering': ['create_time'],
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ongoing', models.BooleanField(default=True)),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('info', models.CharField(max_length=200)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User')),
            ],
            options={
                'verbose_name': '投诉',
                'verbose_name_plural': '投诉',
                'ordering': ['create_time'],
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, default='', upload_to='static/upload/alipay')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='商品价格')),
                ('pay_way', models.IntegerField(choices=[(0, '支付宝'), (1, '微信'), (2, '当面交易')])),
                ('pay_pic', models.ImageField(blank=True, default='', upload_to='static/upload/alipay')),
                ('info', models.CharField(max_length=200)),
                ('sell_times', models.IntegerField(default=0)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User', verbose_name='创建者')),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.File')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'ordering': ['create_time'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.IntegerField(choices=[(0, '等待支付'), (1, '交易完成'), (2, '投诉中'), (3, '交易取消')])),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Good')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='TradeMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('content', models.CharField(max_length=200)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Order')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='index.User')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='index.User')),
            ],
            options={
                'verbose_name': '交易消息',
                'verbose_name_plural': '交易消息',
                'ordering': ['create_time'],
            },
        ),
        migrations.AddField(
            model_name='feedback',
            name='good',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Order'),
        ),
        migrations.AddField(
            model_name='evidence',
            name='feedback',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Feedback'),
        ),
    ]
