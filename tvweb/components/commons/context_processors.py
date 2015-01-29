# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import current_app as app
from . import utilities


def inject_app_data():
    return {
        'app_name': app.config['TABULAR_VALIDATOR_APP_NAME'],
        'domain': app.config['TABULAR_VALIDATOR_DOMAIN'],
        'datetime': utilities.get_datetime(),
    }
