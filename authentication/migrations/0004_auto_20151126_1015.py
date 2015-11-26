# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_plan'),
        ('authentication', '0003_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='age',
        ),
        migrations.RemoveField(
            model_name='client',
            name='overall_score',
        ),
        migrations.AddField(
            model_name='client',
            name='plan',
            field=models.ForeignKey(related_name='Planwise_Clients', default=0, to='administration.Plan'),
            preserve_default=False,
        ),
    ]
