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
from tabular_validator.pipeline import ValidationPipeline
from ..commons import views


class Index(views.APIView):

    """Index of all API endpoints."""

    def data(self, **kwargs):
        data = super(Index, self).data(**kwargs)
        data['endpoints'] = {
            'job_list': url_for('api.job_list'),
        }
        return data


class JobList(views.APIView):

    """Job list view."""

    def data(self, **kwargs):
        data = super(JobList, self).data(**kwargs)
        return data

    def post(self, data, **kwargs):

        # the workspace for all job-related data files
        workspace = os.path.join(app.config['TMP_DIR'], 'workspace')

        # job identifier for this run.
        job_id = request.form.get('job_id') or uuid.uuid4().hex

        # pass the data source
        # TODO: properly handle file uploads
        if isinstance(request.form.get('data_source'), FileStorage):
            data_source = request.form.get('data_source').stream()
        else:
            data_source = request.form.get('data_source')

        # if dry_run, then any files will not be persisted after the job run
        dry_run = request.form.get('dry_run')

        # instantiating the pipeline:
        #     * checks any files are validly formed
        #     * persists them in the workspace under job_id
        # TODO: handling errors raised from instantiating the pipeline
        pipeline = ValidationPipeline(data_source=data_source,
                                      job_id=job_id, dry_run=dry_run,
                                      workspace=workspace)

        # anything after here will be queued in most cases.
        # when queued, the return value will be a Job ID.

        valid, report = pipeline.run()
        data['report'] = report
        data['success'] = valid

        return super(JobList, self).post(data)


class JobDetail(views.APIView):

    """Job detail view."""

    def data(self, **kwargs):
        data = super(JobDetail, self).data(**kwargs)
        return data

    # def post(self, data, **kwargs):
    #     return True
