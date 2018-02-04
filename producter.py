#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from celery_pro.tasks import add

if __name__ == "__main__":
    print add.delay(1, 2)
