# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0008_auto_20191119_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='code',
            field=models.CharField(max_length=6, default=400023),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='users',
            table=None,
        ),
    ]
