# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('deletion_time', models.DateTimeField(default=None, null=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
