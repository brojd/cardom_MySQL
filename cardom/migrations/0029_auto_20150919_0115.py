# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0028_auto_20150919_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='object',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='offers',
            name='province',
            field=models.CharField(max_length=50),
        ),
    ]
