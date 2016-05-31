# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='country',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='state',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
