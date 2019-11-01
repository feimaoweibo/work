# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0003_goods'),
    ]

    operations = [
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
        ),
    ]
