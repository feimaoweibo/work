# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classroom',
            old_name='roomname',
            new_name='name',
        ),
    ]
