# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0008_auto_20160130_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackingsourcedetailsdaily',
            name='web_browser',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'chrome'), (b'2', b'firefox'), (b'4', b'ie'), (b'5', b'opera'), (b'3', b'safari')]),
        ),
        migrations.AddField(
            model_name='trackingsourcedetailslog',
            name='web_browser',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'chrome'), (b'2', b'firefox'), (b'4', b'ie'), (b'5', b'opera'), (b'3', b'safari')]),
        ),
        migrations.AddField(
            model_name='trackingsourcedetailsmonthly',
            name='web_browser',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'chrome'), (b'2', b'firefox'), (b'4', b'ie'), (b'5', b'opera'), (b'3', b'safari')]),
        ),
        migrations.AddField(
            model_name='trackingsourcedetailsweekly',
            name='web_browser',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'chrome'), (b'2', b'firefox'), (b'4', b'ie'), (b'5', b'opera'), (b'3', b'safari')]),
        ),
        migrations.AddField(
            model_name='trackingsourcedetailsyearly',
            name='web_browser',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'chrome'), (b'2', b'firefox'), (b'4', b'ie'), (b'5', b'opera'), (b'3', b'safari')]),
        ),
        migrations.AlterField(
            model_name='trackingsource',
            name='tracking_id',
            field=models.CharField(default=b'GPAL-YeS53r', unique=True, max_length=20),
        ),
    ]
