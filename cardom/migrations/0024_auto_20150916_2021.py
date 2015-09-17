# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0023_auto_20150916_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='rent',
            field=models.IntegerField(default=0, choices=[(0, 'Sprzeda\u017c'), (1, 'Wynajem')]),
        ),
        migrations.AlterField(
            model_name='offersphotos',
            name='offers_id',
            field=models.ForeignKey(to='cardom.Offers', null=True),
        ),
    ]
