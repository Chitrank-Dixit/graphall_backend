# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_auto_20160124_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trackingsource',
            old_name='tags',
            new_name='tag',
        ),
    ]
