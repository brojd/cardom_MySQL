# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0027_auto_20150919_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='object',
            field=models.CharField(default=0, max_length=50, choices=[('Mieszkanie', 'Mieszkanie'), (1, 'Dom'), (2, 'Dzialka'), (3, 'Lokal'), (4, 'Biurowiec')]),
        ),
        migrations.AlterField(
            model_name='offers',
            name='province',
            field=models.CharField(default=0, max_length=50, choices=[('OPOLSKIE', 'OPOLSKIE'), (1, 'DOLNO\u015aL\u0104SKIE'), (2, '\u015aL\u0104SKIE'), (3, 'PODKARPACKIE'), (4, 'LUBUSKIE'), (5, 'LUBELSKIE'), (6, 'MA\u0141OPOLSKIE'), (7, 'KUJAWSKO-POMORSKIE'), (8, 'POMORSKIE'), (9, 'ZACHODNIO-POMORSKIE'), (10, '\u0141\xd3DZKIE'), (11, 'MAZOWIECKIE'), (12, 'PODLASKIE'), (13, 'WIELKOPOLSKIE'), (14, '\u015aWI\u0118TOKRZYSKIE'), (15, 'WARMI\u0143SKO-MAZURSKIE')]),
        ),
        migrations.AlterField(
            model_name='offers',
            name='rent',
            field=models.IntegerField(default=0, choices=[(0, 'Sprzeda\u017c'), (1, 'Wynajem')]),
        ),
    ]
