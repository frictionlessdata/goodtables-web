# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os


DEBUG = True
SECRET_KEY = 'j$p^=yen)f#0lbfg#+*ip^2ufca4@8z1l2$jugael#z+n@ksasas2323h32'
GOODTABLES_NAME = 'Good Tables'
GOODTABLES_STATUS = "Beta"
GOODTABLES_SCHEME = os.environ.get('GOODTABLES_SCHEME', 'http://')
GOODTABLES_DOMAIN = os.environ.get('GOODTABLES_DOMAIN', '127.0.0.1:5000')
GOODTABLES_URL = '{0}{1}'.format(GOODTABLES_SCHEME, GOODTABLES_DOMAIN)
GOODTABLES_SPONSOR = 'Open Knowledge'
GOODTABLES_REPO = 'https://github.com/okfn/goodtables'
GOODTABLES_ISSUES = 'https://github.com/okfn/goodtables-web/issues/new'
GOODTABLES_HELP_REPO = 'https://github.com/okfn/goodtables-web/edit/master/web/theme/templates/pages/help'
GOODTABLES_PIPELINE_DEFAULT_CONFIG = {
    'processors': ('structure', 'schema'),
    'data': None,
    'format': 'csv',
    'dialect': None,
    'options': {
        'structure': {},
        'schema': {}
    },
    'workspace': None,
    'dry_run': True,
    'fail_fast': False,
    'break_on_invalid_processor': False,
}
GOODTABLES_PIPELINE_BUILD_ERROR_RESPONSE = {
    'success': False,
    'error': ('Pipeline build error. One or more '
              'pipeline parameters was invalid.'),
    'meta': {},
    'results': []
}
CONFIG_DIR = os.path.abspath(os.path.dirname(__file__))
CODE_DIR = os.path.abspath(os.path.dirname(CONFIG_DIR))
REPO_DIR = os.path.abspath(os.path.dirname(CODE_DIR))
TMP_DIR = os.path.abspath(os.path.join(REPO_DIR, 'tmp'))
