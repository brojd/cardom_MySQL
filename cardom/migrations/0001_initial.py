# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128, verbose_name=b'Nazwa Kategorii')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=128, verbose_name=b'Miasto')),
                ('province', models.CharField(default=b'OPO', max_length=3, choices=[(b'OPO', b'OPOLSKIE'), (b'DLN', b'DOLNOSLASKIE'), (b'SLK', b'SLASKIE'), (b'PDK', b'PODKARPACKIE'), (b'LBK', b'LUBUSKIE'), (b'LBL', b'LUBELSKIE'), (b'MLP', b'MALOPOLSKIE'), (b'KJP', b'KUJAWSKO-POMORSKIE'), (b'POM', b'POMORSKIE'), (b'ZPM', b'ZACHODNIO-POMORSKIE'), (b'LDZ', b'LODZKIE'), (b'MZW', b'MAZOWIECKIE'), (b'PDL', b'PODLASKIE'), (b'WLK', b'WIELKOPOLSKIE'), (b'SWK', b'SWIETOKRZYSKIE'), (b'WRM', b'WARMINSKO-MAZURSKIE')])),
                ('district', models.CharField(max_length=128, verbose_name=b'Dzielnica')),
                ('nb_rooms', models.IntegerField(verbose_name=b'Liczba pokoi')),
                ('floor_space', models.IntegerField(verbose_name=b'Powierzchnia [m2]')),
                ('price', models.IntegerField(verbose_name=b'cena [zl]')),
                ('category', models.ForeignKey(to='cardom.Category')),
            ],
        ),
    ]
