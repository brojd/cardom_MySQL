# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0031_remove_offers_min_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='object',
            field=models.CharField(default='M', max_length=50, choices=[('D', 'DOM'), ('M', 'MIESZKANIE'), ('L', 'LOKAL'), ('DZ', 'DZIA\u0141KA'), ('O', 'OBIEKT')]),
        ),
        migrations.AlterField(
            model_name='offers',
            name='rent',
            field=models.IntegerField(default=0, choices=[(0, 'SPRZEDA\u017b'), (1, 'WYNAJEM')]),
        ),
    ]
