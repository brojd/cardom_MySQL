# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0032_auto_20150919_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='object',
            field=models.CharField(default='M', max_length=50, choices=[('Mieszkanie', 'MIESZKANIE'), ('Dom', 'DOM'), ('Lokal', 'LOKAL'), ('Dzialka', 'DZIA\u0141KA'), ('Biurowiec', 'OBIEKT')]),
        ),
        migrations.AlterField(
            model_name='offers',
            name='province',
            field=models.CharField(default='OPO', max_length=50, choices=[('OPO', 'OPOLSKIE'), ('DLN', 'DOLNO\u015aL\u0104SKIE'), ('SLK', '\u015aL\u0104SKIE'), ('PDK', 'PODKARPACKIE'), ('LBK', 'LUBUSKIE'), ('LBL', 'LUBELSKIE'), ('MLP', 'MA\u0141OPOLSKIE'), ('KJP', 'KUJAWSKO-POMORSKIE'), ('POM', 'POMORSKIE'), ('ZPM', 'ZACHODNIO-POMORSKIE'), ('LDZ', '\u0141\xd3DZKIE'), ('MZW', 'MAZOWIECKIE'), ('PDL', 'PODLASKIE'), ('WLK', 'WIELKOPOLSKIE'), ('SWK', '\u015aWI\u0118TOKRZYSKIE'), ('WRM', 'WARMI\u0143SKO-MAZURSKIE')]),
        ),
    ]
