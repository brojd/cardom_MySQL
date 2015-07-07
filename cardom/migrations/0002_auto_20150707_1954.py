# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='category',
            field=models.ForeignKey(verbose_name=b'Kategoria', to='cardom.Category'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='province',
            field=models.CharField(default=b'OPO', max_length=3, verbose_name=b'Wojewodztwo', choices=[(b'OPO', b'OPOLSKIE'), (b'DLN', b'DOLNOSLASKIE'), (b'SLK', b'SLASKIE'), (b'PDK', b'PODKARPACKIE'), (b'LBK', b'LUBUSKIE'), (b'LBL', b'LUBELSKIE'), (b'MLP', b'MALOPOLSKIE'), (b'KJP', b'KUJAWSKO-POMORSKIE'), (b'POM', b'POMORSKIE'), (b'ZPM', b'ZACHODNIO-POMORSKIE'), (b'LDZ', b'LODZKIE'), (b'MZW', b'MAZOWIECKIE'), (b'PDL', b'PODLASKIE'), (b'WLK', b'WIELKOPOLSKIE'), (b'SWK', b'SWIETOKRZYSKIE'), (b'WRM', b'WARMINSKO-MAZURSKIE')]),
        ),
    ]
