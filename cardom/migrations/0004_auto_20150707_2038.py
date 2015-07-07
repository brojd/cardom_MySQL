# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0003_auto_20150707_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='transaction',
            field=models.CharField(default=b'S', max_length=1, verbose_name=b'Typ transakcji', choices=[(b'S', b'SPRZEDAZ'), (b'W', b'WYNAJEM')]),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default=b'M', max_length=2, verbose_name=b'Nazwa Kategorii', choices=[(b'D', b'DOMY'), (b'M', b'MIESZKANIA'), (b'L', b'LOKALE'), (b'DZ', b'DZIALKI'), (b'O', b'OBIEKTY')]),
        ),
    ]
