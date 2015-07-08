# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0006_offer_balcony'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('offer', models.ForeignKey(related_name='images', verbose_name=b'zdjecia', to='cardom.Offer')),
            ],
        ),
    ]
