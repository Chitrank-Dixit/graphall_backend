# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20151127_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='user_type',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='masteradmin',
            name='user_type',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='masteradmin',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
