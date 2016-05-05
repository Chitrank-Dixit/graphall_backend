# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_auto_20160113_2212'),
        ('analytics', '0015_auto_20160221_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackingsource',
            name='user',
        ),
        migrations.AddField(
            model_name='trackingsource',
            name='client',
            field=models.ForeignKey(to='authentication.Client', null=True),
        ),
        migrations.AlterField(
            model_name='trackingsource',
            name='tracking_id',
            field=models.CharField(default=b'GPAL-brevwC', unique=True, max_length=20),
        ),
    ]
