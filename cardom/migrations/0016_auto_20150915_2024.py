# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0015_auto_20150915_1919'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offers',
            options={'managed': False},
        ),
    ]
