# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0012_auto_20150721_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='description',
            field=models.TextField(null=True, verbose_name=b'Opis', blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 18, 17, 29, 561000, tzinfo=utc), verbose_name=b'Data publikacji'),
        ),
    ]
