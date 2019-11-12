# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('orderid', models.IntegerField()),
                ('goodsid', models.IntegerField()),
                ('name', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('num', models.IntegerField()),
            ],
            options={
                'db_table': 'detail',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('typeid', models.IntegerField()),
                ('goods', models.CharField(max_length=32)),
                ('company', models.CharField(max_length=50)),
                ('descr', models.TextField()),
                ('price', models.FloatField()),
                ('picname', models.CharField(max_length=255)),
                ('state', models.IntegerField(default=1)),
                ('store', models.IntegerField(default=0)),
                ('num', models.IntegerField(default=0)),
                ('clicknum', models.IntegerField(default=0)),
                ('addtime', models.IntegerField()),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('uid', models.IntegerField()),
                ('linkman', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=6)),
                ('phone', models.CharField(max_length=16)),
                ('addtime', models.IntegerField()),
                ('total', models.FloatField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=32)),
                ('pid', models.IntegerField(default=0)),
                ('path', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'type',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=32)),
                ('sex', models.IntegerField(default=1)),
                ('address', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=6)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=50)),
                ('state', models.IntegerField(default=1)),
                ('addtime', models.IntegerField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
