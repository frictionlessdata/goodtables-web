# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime
from flask.json import JSONEncoder as _JSONEncoder
from . import utilities


class JSONEncoder(_JSONEncoder):

    """Extends Flask's JSONEncoder with more fun things.

    The following features are added:

    * Support for various datetime.* objects
        * Flask only provides support for datetime.datetime objects
        * Hook into our own string format for datetime.* objects

    """

    def default(self, o):

        if isinstance(o, datetime.date):
            return o.strftime(utilities.JSON_DATE_FORMAT)

        if isinstance(o, datetime.time):
            return o.strftime(utilities.JSON_TIME_FORMAT)

        if isinstance(o, datetime.datetime):
            return o.strftime(utilities.JSON_DATETIME_FORMAT)

        # For anything else, let Flask do what it does
        return super(JSONEncoder, self).default(o)
