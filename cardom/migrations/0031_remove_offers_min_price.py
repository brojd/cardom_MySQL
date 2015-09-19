# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0030_offers_min_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offers',
            name='min_price',
        ),
    ]
