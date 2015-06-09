# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import io
import datetime
import pytz
from werkzeug.datastructures import FileStorage
from flask import current_app as app, url_for
from flask.ext.restful import reqparse
from goodtables import pipeline
from goodtables import exceptions
from web import compat


REMOTE_SCHEMES = ('http', 'https', 'ftp', 'ftps')
JSON_DATE_FORMAT = '%Y-%m-%d'
JSON_TIME_FORMAT = '%H:%M:%S'
JSON_DATETIME_FORMAT = '{0}T{1}'.format(JSON_DATE_FORMAT, JSON_TIME_FORMAT)


def get_datetime(date_only=False):
    """Simple wrapper to get a UTC aware `now` or `date`."""
    now = datetime.datetime.now(pytz.utc)
    if date_only:
        return now.date()
    return now


def get_pipeline(runargs=None):
    """Get a pipeline as per config."""
    config = app.config['GOODTABLES_PIPELINE_DEFAULT_CONFIG']
    if runargs:
        config['options']['schema']['schema'] = runargs.pop('schema')
        config['options']['structure']['ignore_empty_rows'] = runargs.pop('ignore_empty_rows')
        config['options']['structure']['ignore_duplicate_rows'] = runargs.pop('ignore_duplicate_rows')
        config.update(runargs)
    try:
        rv = pipeline.Pipeline(**config)
    except exceptions.PipelineBuildError as e:
        rv = None
    return rv


def get_runargs():
    """Get valid args from request."""
    parser = reqparse.RequestParser()
    location = ['json', 'values', 'form', 'args', 'files']
    parser.add_argument('data', location=location)
    parser.add_argument('schema', location=location)
    parser.add_argument('data_url', location=location)
    parser.add_argument('schema_url', location=location)
    parser.add_argument('data_file', type=FileStorage, location=location)
    parser.add_argument('schema_file', type=FileStorage, location=location)
    parser.add_argument('report_limit', type=int, default=1000)
    parser.add_argument('row_limit', type=int, default=20000)
    parser.add_argument('fail_fast', type=bool)
    parser.add_argument('ignore_empty_rows', type=bool)
    parser.add_argument('ignore_duplicate_rows', type=bool)
    parser.add_argument('format')
    parser.add_argument('encoding')
    parser.add_argument('report_type')
    return parser.parse_args()


def get_data_urls():
    """Get valid args from request."""
    parser = reqparse.RequestParser()
    location = ['json', 'values', 'form', 'args', 'files']
    parser.add_argument('data_url', location=location)
    parser.add_argument('schema_url', location=location)
    return parser.parse_args()


def clean_payload(payload):
    payload['data'] = resolve_payload_item('data', payload)
    payload['schema'] = resolve_payload_item('schema', payload)
    del payload['data_url']
    del payload['data_file']
    del payload['schema_url']
    del payload['schema_file']
    return payload


def resolve_payload_item(key, payload):
    """Resolve data or schema from request."""
    as_file = '{0}_file'.format(key)
    as_url = '{0}_url'.format(key)
    if payload.get(key):
        return payload[key]
    if payload.get(as_url):
        return payload[as_url]
    elif payload.get(as_file):
        if key.startswith('data'):
            return payload[as_file].stream
        else:
            return payload[as_file].read().decode('utf-8')
    else:
        return None


def get_report_permalinks(payload):

    if not isinstance(payload['data'], (io.IOBase, FileStorage)) and \
           compat.parse.urlparse(payload['data']).scheme in REMOTE_SCHEMES:
        if not hasattr(payload.get('schema'), 'filename'):
            domain = app.config['GOODTABLES_URL']
            api_fragment = url_for('api.run')
            ui_fragment = url_for('pages.reports')
            params = compat.urlencode({k: v for k, v in payload.items() if v})
            permalinks = {
                'html': '{0}{1}?{2}'.format(domain, ui_fragment, params),
                'json': '{0}{1}?{2}'.format(domain, api_fragment, params)
            }

            return permalinks

    return {}
