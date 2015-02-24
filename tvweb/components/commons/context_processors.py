# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime
from flask import current_app as app


def inject_app_data():
    now = datetime.datetime.now()
    return {
        'name': app.config['TVWEB_NAME'],
        'domain': app.config['TVWEB_URL'],
        'sponsor': app.config['TVWEB_SPONSOR'],
        'new_issue': app.config['TVWEB_REPORT_ISSUE'],
        'datetime': now.strftime('%a %b %d at %I:%M %p'),
        'year': now.year
    }
