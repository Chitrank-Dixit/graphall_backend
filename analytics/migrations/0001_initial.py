# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrackingSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('tracking_id', models.CharField(default=b'GPAL-DBuaKq', unique=True, max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=200)),
                ('industry_category', models.CharField(default=b'1', max_length=1, choices=[(b'7', b'Ecommerce'), (b'1', b'Education'), (b'4', b'Entertainment'), (b'5', b'Government'), (b'2', b'Medical'), (b'6', b'Personal'), (b'8', b'Realestate'), (b'3', b'Sports')])),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('deletion_time', models.DateTimeField(default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('client', models.ForeignKey(to='authentication.Client', null=True)),
                ('master_admin', models.ForeignKey(to='authentication.MasterAdmin', null=True)),
                ('tag', models.ManyToManyField(to='analytics.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrackingSourceDetailsLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('page_url', models.CharField(default=b' ', max_length=200)),
                ('page_views', models.IntegerField(default=0)),
                ('page_clicks', models.IntegerField(default=0)),
                ('web_browser', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'chrome'), (b'2', b'firefox'), (b'4', b'ie'), (b'5', b'opera'), (b'3', b'safari')])),
                ('event_date', models.DateField(auto_now=True, null=True)),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('deletion_time', models.DateTimeField(default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('a', models.CharField(default=b'1', max_length=1)),
                ('tracking_source', models.ForeignKey(to='analytics.TrackingSource')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
