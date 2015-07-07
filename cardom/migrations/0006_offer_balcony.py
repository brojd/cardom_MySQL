# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0005_auto_20150707_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='balcony',
            field=models.BooleanField(default=True),
        ),
    ]
