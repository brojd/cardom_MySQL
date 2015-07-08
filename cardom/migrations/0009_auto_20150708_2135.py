# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0008_auto_20150708_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='promoted',
            field=models.BooleanField(default=False, verbose_name=b'Promowana'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='balcony',
            field=models.BooleanField(default=True, verbose_name=b'Balkon'),
        ),
    ]
