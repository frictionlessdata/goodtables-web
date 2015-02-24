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
from ..commons import view_mixins


class Main(restful.Resource):

    """Index of all API endpoints."""

    def get(self):
        return {
            'endpoints': {
                'index': url_for('api.main'),
                'run': url_for('api.run')
            }
        }


class Run(restful.Resource, view_mixins.RunPipelineMixin):

    """GET a list of jobs, and POST to create a job."""

    def get(self):
        # we allow GET requests for pipeline runs, so:
        if request.args:
            return self.run_pipeline()
        return {}

    def post(self):
        """POST a new job, which submits a data source for validation."""
        return self.run_pipeline()
