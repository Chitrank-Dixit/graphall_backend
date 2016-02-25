# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0010_auto_20160204_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackingsource',
            name='tracking_id',
            field=models.CharField(default=b'GPAL-tTOwEb', unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='trackingsourcedetailsdaily',
            name='page_url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trackingsourcedetailslog',
            name='page_url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trackingsourcedetailsmonthly',
            name='page_url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trackingsourcedetailsweekly',
            name='page_url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trackingsourcedetailsyearly',
            name='page_url',
            field=models.CharField(max_length=200),
        ),
    ]
