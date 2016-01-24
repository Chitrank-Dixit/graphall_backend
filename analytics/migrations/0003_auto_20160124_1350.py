# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_auto_20160116_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackingSourceDetailsDaily',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_url', models.CharField(unique=True, max_length=200)),
                ('page_views', models.IntegerField()),
                ('page_clicks', models.IntegerField()),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('deletion_time', models.DateTimeField(default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('day', models.CharField(default=b'1', max_length=1, choices=[(b'5', b'Friday'), (b'1', b'Monday'), (b'6', b'Saturday'), (b'7', b'Sunday'), (b'4', b'Thursday'), (b'2', b'Tuesday'), (b'3', b'Wednesday')])),
                ('tracking_source', models.ForeignKey(to='analytics.TrackingSource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrackingSourceDetailsLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_url', models.CharField(unique=True, max_length=200)),
                ('page_views', models.IntegerField()),
                ('page_clicks', models.IntegerField()),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('deletion_time', models.DateTimeField(default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('a', models.CharField(max_length=1)),
                ('tracking_source', models.ForeignKey(to='analytics.TrackingSource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrackingSourceDetailsMonthly',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_url', models.CharField(unique=True, max_length=200)),
                ('page_views', models.IntegerField()),
                ('page_clicks', models.IntegerField()),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('deletion_time', models.DateTimeField(default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('month', models.CharField(default=b'1', max_length=1, choices=[(b'4', b'April'), (b'8', b'August'), (b'12', b'December'), (b'2', b'February'), (b'1', b'January'), (b'7', b'July'), (b'6', b'June'), (b'3', b'March'), (b'5', b'May'), (b'11', b'November'), (b'10', b'October'), (b'9', b'September')])),
                ('tracking_source', models.ForeignKey(to='analytics.TrackingSource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrackingSourceDetailsWeekly',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_url', models.CharField(unique=True, max_length=200)),
                ('page_views', models.IntegerField()),
                ('page_clicks', models.IntegerField()),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('deletion_time', models.DateTimeField(default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('a', models.CharField(max_length=1)),
                ('tracking_source', models.ForeignKey(to='analytics.TrackingSource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrackingSourceDetailsYearly',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_url', models.CharField(unique=True, max_length=200)),
                ('page_views', models.IntegerField()),
                ('page_clicks', models.IntegerField()),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('deletion_time', models.DateTimeField(default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('year', models.DateTimeField(default=2016)),
                ('tracking_source', models.ForeignKey(to='analytics.TrackingSource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='trackingsourcedetails',
            name='tracking_source',
        ),
        migrations.DeleteModel(
            name='TrackingSourceDetails',
        ),
    ]
