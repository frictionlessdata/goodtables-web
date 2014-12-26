from flask import current_app as app
from . import utilities


def inject_app_data():
    return {
        'app_name': app.config['TABLE_VALIDATION_APP_NAME'],
        'domain': app.config['TABLE_VALIDATION_DOMAIN'],
        'datetime': utilities.get_datetime(),
    }
