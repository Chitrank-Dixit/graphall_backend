# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'permissions': (('administration.browse_revision_plan', 'Can browse revisions'), ('administration.reapply_revision_plan', 'Can repply revision'))},
        ),
    ]
