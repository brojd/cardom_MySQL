# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0010_offer_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerimage',
            name='main_image',
            field=models.BooleanField(default=False, verbose_name=b'zdjecie glowne'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 11, 4, 58, 502000, tzinfo=utc), verbose_name=b'Data publikacji'),
        ),
    ]
