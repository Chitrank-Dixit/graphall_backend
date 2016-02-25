# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0011_auto_20160208_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackingsourcedetailsdaily',
            name='event_time',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='trackingsourcedetailslog',
            name='event_time',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='trackingsourcedetailsmonthly',
            name='event_time',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='trackingsourcedetailsweekly',
            name='event_time',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='trackingsourcedetailsyearly',
            name='event_time',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='trackingsource',
            name='tracking_id',
            field=models.CharField(default=b'GPAL-EUITTt', unique=True, max_length=20),
        ),
    ]
