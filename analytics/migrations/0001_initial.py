# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrackingSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tracking_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=200)),
                ('industry_category', models.CharField(default=b'1', max_length=1, choices=[(b'7', b'Ecommerce'), (b'1', b'Education'), (b'4', b'Entertainment'), (b'5', b'Government'), (b'2', b'Medical'), (b'6', b'Personal'), (b'8', b'Realestate'), (b'3', b'Sports')])),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('deletion_time', models.DateTimeField(default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrackingSourceDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_url', models.CharField(max_length=200)),
                ('page_views', models.IntegerField()),
                ('page_clicks', models.IntegerField()),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('deletion_time', models.DateTimeField(default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('tracking_source', models.ForeignKey(to='analytics.TrackingSource')),
            ],
        ),
    ]
