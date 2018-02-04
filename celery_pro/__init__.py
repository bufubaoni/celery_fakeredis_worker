#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from celery import Celery

app = Celery('tasks', broker='redis://', backend='redis://', include=['celery_pro.tasks'])
