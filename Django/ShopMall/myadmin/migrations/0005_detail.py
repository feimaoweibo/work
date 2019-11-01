# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0004_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ordersid', models.IntegerField()),
                ('goodsid', models.IntegerField()),
                ('name', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('num', models.IntegerField()),
            ],
        ),
    ]
