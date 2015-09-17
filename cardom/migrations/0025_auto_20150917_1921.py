# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0024_auto_20150916_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='area',
            field=models.DecimalField(max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='offers',
            name='price',
            field=models.DecimalField(max_digits=18, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='offers',
            name='price_square',
            field=models.DecimalField(max_digits=18, decimal_places=0),
        ),
    ]
