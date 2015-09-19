# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0025_auto_20150917_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='province',
            field=models.IntegerField(default=0, choices=[(1, 'OPOLSKIE'), (2, 'DOLNO\u015aL\u0104SKIE'), (3, '\u015aL\u0104SKIE'), (4, 'PODKARPACKIE'), (5, 'LUBUSKIE'), (6, 'LUBELSKIE'), (7, 'MA\u0141OPOLSKIE'), (8, 'KUJAWSKO-POMORSKIE'), (9, 'POMORSKIE'), (10, 'ZACHODNIO-POMORSKIE'), (11, '\u0141\xd3DZKIE'), (12, 'MAZOWIECKIE'), (13, 'PODLASKIE'), (14, 'WIELKOPOLSKIE'), (15, '\u015aWI\u0118TOKRZYSKIE'), (16, 'WARMI\u0143SKO-MAZURSKIE')]),
        ),
    ]
