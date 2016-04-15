# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
