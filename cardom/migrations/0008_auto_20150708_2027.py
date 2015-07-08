# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0007_offerimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerimage',
            name='images',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'zdjecia', blank=True),
        ),
        migrations.AlterField(
            model_name='offerimage',
            name='offer',
            field=models.ForeignKey(related_name='images', to='cardom.Offer'),
        ),
    ]
