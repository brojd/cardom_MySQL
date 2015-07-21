# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0011_auto_20150712_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerimage',
            name='main_image',
        ),
        migrations.AddField(
            model_name='offer',
            name='main_image',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'Zdj\xc4\x99cie g\xc5\x82\xc3\xb3wne', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default=b'M', max_length=2, verbose_name=b'Nazwa Kategorii', choices=[(b'D', b'DOM'), (b'M', b'MIESZKANIE'), (b'L', b'LOKAL'), (b'DZ', b'DZIA\xc5\x81KA'), (b'O', b'OBIEKT')]),
        ),
        migrations.AlterField(
            model_name='offer',
            name='category',
            field=models.ForeignKey(verbose_name=b'Rodzaj obiektu', to='cardom.Category'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 18, 16, 46, 283000, tzinfo=utc), verbose_name=b'Data publikacji'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='transaction',
            field=models.CharField(default=b'S', max_length=1, verbose_name=b'Typ transakcji', choices=[(b'S', b'SPRZEDA\xc5\xbb'), (b'W', b'WYNAJEM')]),
        ),
        migrations.AlterField(
            model_name='offerimage',
            name='images',
            field=models.ImageField(upload_to=b'photos/', null=True, verbose_name=b'zdjecia', blank=True),
        ),
    ]
