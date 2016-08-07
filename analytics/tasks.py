from __future__ import absolute_import

from celery import shared_task
import json

@shared_task
def add(x, y):
    return x + y #json.dumps({'result':x + y})

