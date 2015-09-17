# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0022_auto_20150915_2126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offers',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='offersphotos',
            options={'managed': True},
        ),
    ]
