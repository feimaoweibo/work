# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0009_auto_20191120_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='ordersid',
            new_name='orderid',
        ),
    ]
