# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import io
import uuid
from werkzeug.datastructures import FileStorage
from flask import current_app as app, url_for, request
from flask.ext import restful
from flask.ext.restful import reqparse, inputs
from tabular_validator import pipeline
from ..core import api


class Index(restful.Resource):

    """Index of all API endpoints."""

    def get(self):
        data = {
            'endpoints': {
                'job_list': url_for('job_list')
            }
        }
        return data


class JobList(restful.Resource):

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

        table_schema_source = request.form.get('table_schema_source', None)

        # if dry_run, no files will be persisted
        dry_run = request.form.get('dry_run', True)

        # build out the options object
        options = {
            'tableschema': {
                'table_schema_source': table_schema_source
            }
        }

        # build and run a validation pipeline
        try:
            validator = pipeline.ValidationPipeline(data_source=data_source,
                                                    dry_run=dry_run,
                                                    options=options,
                                                    workspace=workspace)
        except Exception as e:
            data = {
                'status': 400,
                'message': 'Could not create a pipeline instance'
            }
            return data, 400

        valid, report = validator.run()
        data = {
            'success': valid,
            'report': report
        }
        return data


api.add_resource(Index, '/', endpoint='index')
api.add_resource(JobList, '/jobs', endpoint='job_list')
