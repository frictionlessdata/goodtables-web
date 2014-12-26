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
