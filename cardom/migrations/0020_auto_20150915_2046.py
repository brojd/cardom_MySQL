# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0019_auto_20150915_2040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offers',
            options={'managed': False},
        ),
    ]
