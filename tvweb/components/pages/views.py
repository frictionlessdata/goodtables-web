# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import (current_app as app, request, redirect, url_for, views,
                   render_template)
from ..commons import utilities
from ..commons import view_mixins
from . import forms


class Main(views.MethodView):

    """Return the front page."""

    template = 'pages/main.html'
    form_class = forms.RunForm

    def get_data(self, **kwargs):
        return {
            'form': self.form_class()
        }

    def get(self, **kwargs):
        return render_template(self.template, **self.get_data(**kwargs))


class Report(views.MethodView, view_mixins.RunPipelineMixin):

    """Return a Report."""

    template = 'pages/report.html'
    form_class = forms.RunForm

    def get_data(self, **kwargs):
        return {
            'form': self.form_class(),
            'report': None,
            'permalinks': {}
        }

    def get(self, **kwargs):
        data = self.get_data(**kwargs)
        if request.args:
            data.update(self.run_pipeline(with_permalinks=True))
            data.update(self._process_report_data(data['report']))
        return render_template(self.template, **data)

    def post(self, **kwargs):
        data = self.get_data(**kwargs)
        if data['form'].validate_on_submit():
            data.update(self.run_pipeline(with_permalinks=True))
            data.update(self._process_report_data(data['report']))
        return render_template(self.template, **data)

    def _process_report_data(self, report):

        def flatten_results(report):
            """Flatten results in a report for Web UI."""
            raw_results = report['results']

            return raw_results

        flat_results = flatten_results(report)
        flat_result_count = len(flat_results)

        if flat_result_count > 20:
            result_detail_phrase = 'first {0}'.format(flat_result_count)
        else:
            result_detail_phrase = '{0}'.format(flat_result_count)

        processed = {
            'summary': report['summary'],
            'columns': report['summary']['columns'],
            'header_index': report['summary']['header_index'],
            'row_count': report['summary']['total_row_count'],
            'column_count': len(report['summary']['columns']),
            'bad_column_percent': int((report['summary']['bad_column_count'] / len(report['summary']['columns'])) * 100),
            'bad_row_percent': int((report['summary']['bad_row_count'] / report['summary']['total_row_count']) * 100),
            'bad_cell_count': 'NaN',
            'flat_results': flat_results,
            'flat_result_count': flat_result_count,
            'result_detail_phrase': result_detail_phrase
        }

        return processed


class Help(views.MethodView):

    """Return a Help page."""

    template = 'pages/help.html'

    def get_data(self, **kwargs):
        return {}

    def get(self, **kwargs):
        return render_template(self.template, **self.get_data(**kwargs))
