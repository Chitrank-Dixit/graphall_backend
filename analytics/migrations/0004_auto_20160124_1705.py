# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_auto_20160124_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackingsourcedetailsyearly',
            name='year',
        ),
        migrations.AddField(
            model_name='trackingsourcedetailsyearly',
            name='a',
            field=models.CharField(default=b'1', max_length=1),
        ),
        migrations.AlterField(
            model_name='trackingsourcedetailslog',
            name='a',
            field=models.CharField(default=b'1', max_length=1),
        ),
        migrations.AlterField(
            model_name='trackingsourcedetailsweekly',
            name='a',
            field=models.CharField(default=b'1', max_length=1),
        ),
    ]
