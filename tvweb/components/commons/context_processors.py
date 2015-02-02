# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import current_app as app


def inject_app_data():
    return {
        'app_name': app.config['TVWEB_APP_NAME'],
        'domain': app.config['TVWEB_DOMAIN'],
    }
