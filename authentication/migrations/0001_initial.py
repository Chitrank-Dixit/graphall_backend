# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('place_id', models.CharField(max_length=100, blank=True)),
                ('geo_coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('pin_code', models.CharField(max_length=20, blank=True)),
                ('address', models.TextField(max_length=200, blank=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('registered_type', models.IntegerField(default=0)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999999'. Up to 15 digits allowed.")])),
                ('website', models.CharField(max_length=100)),
                ('user_type', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'client'), (b'2', b'masteradmin')])),
                ('access_level', models.CharField(max_length=1, choices=[(b'1', b'admin'), (b'2', b'manager')])),
                ('plan', models.ForeignKey(related_name='planwise_clients', to='administration.Plan', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MasterAdmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registered_type', models.IntegerField(default=0)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999999'. Up to 15 digits allowed.")])),
                ('website', models.CharField(max_length=100)),
                ('user_type', models.CharField(default=b'2', max_length=1, choices=[(b'1', b'client'), (b'2', b'masteradmin')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
