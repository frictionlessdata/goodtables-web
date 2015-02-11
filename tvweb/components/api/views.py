# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import io
import uuid
from werkzeug.datastructures import FileStorage
from flask import current_app as app, request, url_for
from flask.ext import restful
from flask.ext.restful import inputs, reqparse
from ..commons import utilities


class Main(restful.Resource):

    """Index of all API endpoints."""

    def get(self):
        data = {
            'endpoints': {
                'run': url_for('api.run')
            }
        }
        return data


class Run(restful.Resource):

    """GET a list of jobs, and POST to create a job."""

    def get(self):
        return {}

    def post(self):
        """POST a new job, which submits a data source for validation."""

        parser = reqparse.RequestParser()
        parser.add_argument('data_source', required=True,
                            type=inputs.url,
                            help='data_source must be a valid URL.')
        parser.add_argument('table_schema_source',  # type=inputs.url,
                            help='table_schema_source must be a valid URL.')
        parser.add_argument('dry_run', type=inputs.boolean,
                            help='dry_run must be a boolean.')
        args = parser.parse_args()

        # the workspace for all job-related data files
        workspace = os.path.join(app.config['TMP_DIR'])

        # pass the data source
        if isinstance(request.form.get('data_source'), FileStorage):
            data_source = request.form.get('data_source').stream()
        else:
            data_source = request.form.get('data_source')

        # build and run a validation pipeline
        pipeline = utilities.get_pipeline()  # config goes in too
        if pipeline is None:
            return app.config['PIPELINE_BUILD_ERROR_RESPONSE'], 400

        valid, report = pipeline.run()
        data = {
            'success': valid,
            'status': 200,
            'report': report
        }
        return data
