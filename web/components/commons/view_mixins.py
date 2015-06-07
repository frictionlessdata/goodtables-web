# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
from werkzeug.datastructures import FileStorage
from flask import current_app as app
from goodtables.pipeline import Pipeline
from . import utilities


class RunPipelineMixin(object):

    def run_pipeline(self, with_permalinks=False):

        payload = utilities.clean_payload(utilities.get_runargs())
        data = {}
        data['sources'] = utilities.get_data_urls()
        data['success'] = False
        data['report'] = app.config['GOODTABLES_PIPELINE_BUILD_ERROR_RESPONSE']

        if with_permalinks:
            data['permalinks'] = utilities.get_report_permalinks(payload)

        if isinstance(payload['data'], FileStorage):
            payload['data'] = payload['data'].stream

        # build and run a validation pipeline
        try:
            pipeline = utilities.get_pipeline(payload)
        except Exception as e:
            pipeline = None
            data['report']['error_title'] = e.__class__.__name__
            data['report']['error_message'] = e.msg

        if isinstance(pipeline, Pipeline):
            success, report = pipeline.run()
            data.update({'success': success, 'report': report.generate()})

        return data
