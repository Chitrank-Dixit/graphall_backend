# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_auto_20151226_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='user_type',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'client'), (b'2', b'masteradmin')]),
        ),
        migrations.AlterField(
            model_name='masteradmin',
            name='user_type',
            field=models.CharField(default=b'2', max_length=1, choices=[(b'1', b'client'), (b'2', b'masteradmin')]),
        ),
    ]
