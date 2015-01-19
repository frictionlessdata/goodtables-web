import os


DEBUG = True

SECRET_KEY = 'j$p^=yen)f#0lbfg#+*ip^2ufca4@8z1l2$jugael#z+n@ksasas2323h32'

TABULAR_VALIDATOR_APP_NAME = 'Table Validation API'

TABULAR_VALIDATOR_DOMAIN = '{0}://{1}'.format('https', '127.0.0.1:5000')

TABULAR_VALIDATOR_FLASH_CATEGORIES = {
    'info': 'info',
    'success': 'success',
    'warning': 'warning',
    'error': 'danger'
}

CONFIG_DIR = os.path.abspath(os.path.dirname(__file__))
CODE_DIR = os.path.abspath(os.path.dirname(CONFIG_DIR))
REPO_DIR = os.path.abspath(os.path.dirname(CODE_DIR))
TMP_DIR = os.path.abspath(os.path.join(REPO_DIR, 'tmp'))
