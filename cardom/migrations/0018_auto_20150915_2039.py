# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0017_auto_20150915_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offers',
            old_name='latitude',
            new_name='latitu',
        ),
    ]
