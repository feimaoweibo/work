# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_auto_20191016_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='loc',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='course',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
