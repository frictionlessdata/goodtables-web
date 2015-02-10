import os
import io
import uuid
from werkzeug.datastructures import FileStorage
from flask import current_app as app, request, url_for
from flask.ext import restful
from flask.ext.restful import inputs, reqparse
from tabular_validator import pipeline


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

        table_schema_source = request.form.get('table_schema_source', None)

        # if dry_run, no files will be persisted
        dry_run = True  # request.form.get('dry_run', True)

        # build out the options object
        options = {
            'tableschema': {
                'table_schema_source': table_schema_source
            }
        }

        # the validators in the pipeline
        validators = ('structure', 'tableschema')

        # build and run a validation pipeline
        try:
            validator = pipeline.ValidationPipeline(validators=validators,
                                                    data_source=data_source,
                                                    dry_run=dry_run,
                                                    options=options,
                                                    workspace=workspace)
        except Exception as e:
            data = {
                'status': 400,
                'message': 'Failed to instantiate the pipeline: {0}'.format(e)
            }
            return data, 400

        valid, report = validator.run()
        data = {
            'success': valid,
            'report': report
        }
        return data
