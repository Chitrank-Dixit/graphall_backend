# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_auto_20160531_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackingsource',
            name='creation_time',
        ),
        migrations.RemoveField(
            model_name='trackingsource',
            name='deletion_time',
        ),
        migrations.RemoveField(
            model_name='trackingsourcedetailslog',
            name='creation_time',
        ),
        migrations.RemoveField(
            model_name='trackingsourcedetailslog',
            name='deletion_time',
        ),
        migrations.AlterField(
            model_name='trackingsource',
            name='tracking_id',
            field=models.CharField(default=b'GPAL-jZVBSv', unique=True, max_length=20),
        ),
    ]
