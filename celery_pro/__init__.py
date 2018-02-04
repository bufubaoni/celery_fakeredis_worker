#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import sys
import os
PACKAGE_PATH = os.path.dirname(os.path.dirname(__file__))

sys.path.append(PACKAGE_PATH)

from celery import Celery  # noqa

# default transport kombu.transport.redis.Transport


# custom transport fkredis.transport.Transport
# from fkredis.transport import Transport
app = Celery('tasks', broker='fkredis.transport.Transport+redis://',
             backend='redis://', include=['celery_pro.tasks'])
