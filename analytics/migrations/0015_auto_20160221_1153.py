# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0014_auto_20160210_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackingsourcedetailsdaily',
            name='tracking_source',
        ),
        migrations.RemoveField(
            model_name='trackingsourcedetailsmonthly',
            name='tracking_source',
        ),
        migrations.RemoveField(
            model_name='trackingsourcedetailsweekly',
            name='tracking_source',
        ),
        migrations.RemoveField(
            model_name='trackingsourcedetailsyearly',
            name='tracking_source',
        ),
        migrations.AlterField(
            model_name='trackingsource',
            name='tracking_id',
            field=models.CharField(default=b'GPAL-hUZIHU', unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='trackingsourcedetailslog',
            name='page_clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trackingsourcedetailslog',
            name='page_url',
            field=models.CharField(default=b' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='trackingsourcedetailslog',
            name='page_views',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='TrackingSourceDetailsDaily',
        ),
        migrations.DeleteModel(
            name='TrackingSourceDetailsMonthly',
        ),
        migrations.DeleteModel(
            name='TrackingSourceDetailsWeekly',
        ),
        migrations.DeleteModel(
            name='TrackingSourceDetailsYearly',
        ),
    ]
