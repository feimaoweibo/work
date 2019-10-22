# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('update_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('username', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('gender', models.IntegerField(default=1)),
                ('address', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=30)),
                ('state', models.IntegerField(default=1)),
            ],
        ),
    ]
