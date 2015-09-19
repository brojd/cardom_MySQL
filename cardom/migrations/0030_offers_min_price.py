# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0029_auto_20150919_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='min_price',
            field=models.IntegerField(null=True),
        ),
    ]
