# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0013_auto_20160210_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackingsource',
            name='tracking_id',
            field=models.CharField(default=b'GPAL-U933v9', unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='trackingsourcedetailsdaily',
            name='day',
            field=models.CharField(default=b'1', max_length=1, null=True, choices=[(b'5', b'Friday'), (b'1', b'Monday'), (b'6', b'Saturday'), (b'7', b'Sunday'), (b'4', b'Thursday'), (b'2', b'Tuesday'), (b'3', b'Wednesday')]),
        ),
    ]
