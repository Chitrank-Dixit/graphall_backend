# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackingsource',
            name='tracking_id',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='trackingsourcedetails',
            name='page_url',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]