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
        # we allow GET requests for pipeline runs, so:
        if request.args:
            return self.run_pipeline()
        return {}

    def post(self):
        """POST a new job, which submits a data source for validation."""
        return self.run_pipeline()

    def run_pipeline(self):

        payload = utilities.clean_payload(utilities.get_runargs())
        data = {}

        # the workspace for all job-related data files
        workspace = os.path.join(app.config['TMP_DIR'])

        if isinstance(payload['data'], FileStorage):
            payload['data'] = payload['data'].read().decode('utf-8')

        # build and run a validation pipeline
        pipeline = utilities.get_pipeline(payload)
        if pipeline is None:
            data.update({'success': False,
                         'report': app.config['TVWEB_PIPELINE_BUILD_ERROR_RESPONSE']})
        else:
            success, report = pipeline.run()
            data.update({'success': success, 'report': report})

        return data
