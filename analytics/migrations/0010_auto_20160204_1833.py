# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0009_auto_20160201_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackingsource',
            name='tracking_id',
            field=models.CharField(default=b'GPAL-sFmmAR', unique=True, max_length=20),
        ),
    ]
