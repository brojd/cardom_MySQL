# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0034_auto_20150919_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='object',
            field=models.CharField(default='M', max_length=50, verbose_name='MIESZKANIE', choices=[('Mieszkanie', 'MIESZKANIE'), ('Dom', 'DOM'), ('Lokal', 'LOKAL'), ('Dzialka', 'DZIA\u0141KA'), ('Biurowiec', 'OBIEKT')]),
        ),
        migrations.AlterField(
            model_name='offers',
            name='province',
            field=models.CharField(max_length=50, choices=[('OPOLSKIE', 'OPOLSKIE'), ('DOLNO\u015aL\u0104SKIE', 'DOLNO\u015aL\u0104SKIE'), ('\u015aL\u0104SKIE', '\u015aL\u0104SKIE')]),
        ),
    ]
