# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0004_auto_20150707_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='transaction',
        ),
        migrations.AddField(
            model_name='offer',
            name='transaction',
            field=models.CharField(default=b'S', max_length=1, verbose_name=b'Typ transakcji', choices=[(b'S', b'SPRZEDAZ'), (b'W', b'WYNAJEM')]),
        ),
    ]
