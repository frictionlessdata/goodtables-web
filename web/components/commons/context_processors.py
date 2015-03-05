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
        'name': app.config['GOODTABLES_NAME'],
        'status': app.config['GOODTABLES_STATUS'],
        'domain': app.config['GOODTABLES_URL'],
        'sponsor': app.config['GOODTABLES_SPONSOR'],
        'repo': app.config['GOODTABLES_REPO'],
        'new_issue': app.config['GOODTABLES_ISSUES'],
        'datetime': now.strftime('%a %b %d at %I:%M %p'),
        'year': now.year
    }
