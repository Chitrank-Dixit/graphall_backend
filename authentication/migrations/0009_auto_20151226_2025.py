# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20151201_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='plan',
            field=models.ForeignKey(related_name='planwise_clients', to='administration.Plan', null=True),
        ),
    ]
