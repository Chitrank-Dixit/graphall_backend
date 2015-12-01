# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20151128_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='mobile_phone',
        ),
        migrations.RemoveField(
            model_name='masteradmin',
            name='mobile_phone',
        ),
        migrations.AddField(
            model_name='client',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999999'. Up to 15 digits allowed.")]),
        ),
        migrations.AddField(
            model_name='masteradmin',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999999'. Up to 15 digits allowed.")]),
        ),
    ]
