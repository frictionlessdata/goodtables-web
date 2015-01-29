# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import datetime
import json
import pytz


JSON_DATE_FORMAT = '%Y-%m-%d'
JSON_TIME_FORMAT = '%H:%M:%S'
JSON_DATETIME_FORMAT = '{0}T{1}'.format(JSON_DATE_FORMAT, JSON_TIME_FORMAT)


def get_datetime(date_only=False):
    """Simple wrapper to get a UTC aware `now` or `date`."""
    now = datetime.datetime.now(pytz.utc)
    if date_only:
        return now.date()
    return now
