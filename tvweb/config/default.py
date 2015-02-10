# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os


DEBUG = True
SECRET_KEY = 'j$p^=yen)f#0lbfg#+*ip^2ufca4@8z1l2$jugael#z+n@ksasas2323h32'
TVWEB_NAME = 'Table Validation'
TVWEB_DOMAIN = '{0}://{1}'.format('https', '127.0.0.1:5000')
TVWEB_SPONSOR = 'Open Knowledge'
CONFIG_DIR = os.path.abspath(os.path.dirname(__file__))
CODE_DIR = os.path.abspath(os.path.dirname(CONFIG_DIR))
REPO_DIR = os.path.abspath(os.path.dirname(CODE_DIR))
TMP_DIR = os.path.abspath(os.path.join(REPO_DIR, 'tmp'))
