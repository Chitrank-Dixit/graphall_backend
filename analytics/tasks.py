from __future__ import absolute_import
from celery.schedules import crontab
from celery import shared_task
from celery.task import periodic_task
from celery.utils.log import get_task_logger
import json

logger = get_task_logger(__name__)

@shared_task
def add(x, y):
    return json.dumps({'result':x + y})


@periodic_task(run_every=crontab())
def gen_prime(x):
    logger.info("Start prime task")
    multiples = []
    results = []
    for i in xrange(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in xrange(i*i, x+1, i):
                multiples.append(j)
    logger.info("Finish prime task")
    return results