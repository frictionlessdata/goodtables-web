# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os


DEBUG = True
SECRET_KEY = 'j$p^=yen)f#0lbfg#+*ip^2ufca4@8z1l2$jugael#z+n@ksasas2323h32'
TVWEB_NAME = 'Table Validation'
TVWEB_DOMAIN = '{0}://{1}'.format('http', '127.0.0.1:5000')
TVWEB_SPONSOR = 'Open Knowledge'
TVWEB_REPORT_ISSUE = 'https://github.com/okfn/tabular-validator-web/issues/new'
TVWEB_PIPELINE_DEFAULT_CONFIG = {
    'validators': ('structure', 'schema'),
    'data': None,
    'format': 'csv',
    'dialect': None,
    'options': {
        'structure': {},
        'schema': {}
    },
    'workspace': None,
    'dry_run': True,
}
TVWEB_PIPELINE_BUILD_ERROR_RESPONSE = {
    'success': False,
    'meta': {
        'message': ('Pipeline build error. One or more '
                    'pipeline parameters was invalid.')
    }
}
CONFIG_DIR = os.path.abspath(os.path.dirname(__file__))
CODE_DIR = os.path.abspath(os.path.dirname(CONFIG_DIR))
REPO_DIR = os.path.abspath(os.path.dirname(CODE_DIR))
TMP_DIR = os.path.abspath(os.path.join(REPO_DIR, 'tmp'))
