# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0018_auto_20150915_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offers',
            old_name='latitu',
            new_name='latitude',
        ),
    ]
