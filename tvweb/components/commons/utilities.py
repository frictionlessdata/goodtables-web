# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import io
import datetime
import json
import pytz
from werkzeug.datastructures import FileStorage
from flask import current_app as app, url_for
from flask.ext.restful import reqparse
from tabular_validator import pipeline
from tabular_validator import exceptions
from tvweb import compat


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
    config = app.config['TVWEB_PIPELINE_DEFAULT_CONFIG']
    if runargs:
        config['options']['schema']['schema'] = runargs.pop('schema')
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
        return payload[as_file].read().decode('utf-8')
    else:
        return None


def get_reporturl(payload):
    if payload.get('data_url'):
        if not payload.get('schema_file').filename:
            domain = app.config['TVWEB_DOMAIN']
            run = url_for('api.run')
            params = compat.urlencode({'data': payload['data_url'], 'schema': payload['schema_url']})
            return '{0}{1}?{2}'.format(domain, run, params)
    return None
