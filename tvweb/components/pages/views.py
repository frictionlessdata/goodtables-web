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
        return render_template(self.template, **data)

    def post(self, **kwargs):
        data = self.get_data(**kwargs)
        if data['form'].validate_on_submit():
            data.update(self.run_pipeline(with_permalinks=True))
        return render_template(self.template, **data)


class Help(views.MethodView):

    """Return a Help page."""

    template = 'pages/help.html'

    def get_data(self, **kwargs):
        return {}

    def get(self, **kwargs):
        return render_template(self.template, **self.get_data(**kwargs))
