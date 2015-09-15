# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0021_auto_20150915_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offersproperties',
            name='offers_id',
            field=models.ForeignKey(to='cardom.Offers'),
        ),
        migrations.AlterField(
            model_name='offersproperties',
            name='properties_id',
            field=models.ForeignKey(to='cardom.Properties'),
        ),
    ]
