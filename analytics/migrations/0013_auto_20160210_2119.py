# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0012_auto_20160210_2117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trackingsourcedetailsdaily',
            old_name='event_time',
            new_name='event_date',
        ),
        migrations.RenameField(
            model_name='trackingsourcedetailslog',
            old_name='event_time',
            new_name='event_date',
        ),
        migrations.RenameField(
            model_name='trackingsourcedetailsmonthly',
            old_name='event_time',
            new_name='event_date',
        ),
        migrations.RenameField(
            model_name='trackingsourcedetailsweekly',
            old_name='event_time',
            new_name='event_date',
        ),
        migrations.RenameField(
            model_name='trackingsourcedetailsyearly',
            old_name='event_time',
            new_name='event_date',
        ),
        migrations.AlterField(
            model_name='trackingsource',
            name='tracking_id',
            field=models.CharField(default=b'GPAL-ESP94o', unique=True, max_length=20),
        ),
    ]
