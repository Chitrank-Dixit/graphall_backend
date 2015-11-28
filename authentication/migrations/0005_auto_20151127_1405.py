# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0004_auto_20151126_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterAdmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registered_type', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=100)),
                ('mobile_phone', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='mobile_phone',
            field=models.IntegerField(default=0),
        ),
    ]
