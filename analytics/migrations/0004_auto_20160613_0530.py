# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_auto_20160612_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackingsourcedetailslog',
            name='a',
        ),
        migrations.AlterField(
            model_name='trackingsource',
            name='tracking_id',
            field=models.CharField(default=b'GPAL-iKxxmn', unique=True, max_length=20),
        ),
    ]
