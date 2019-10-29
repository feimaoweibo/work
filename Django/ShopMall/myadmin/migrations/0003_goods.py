# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_types'),
    ]

    operations = [
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
        ),
    ]
