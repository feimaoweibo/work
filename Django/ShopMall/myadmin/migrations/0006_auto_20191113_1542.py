# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0005_detail'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='users',
            table='users',
        ),
    ]
