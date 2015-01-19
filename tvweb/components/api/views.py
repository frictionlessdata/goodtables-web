import os
import io
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

        temp = os.path.join(app.config['TMP_DIR'], 'temp')

        with io.open(temp, mode='w+b') as f:
            request.files['data_source'].save(f)

        data_source = io.open(temp, mode='r+t', encoding='utf-8')
        pipeline = ValidationPipeline(data_source=data_source)
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
