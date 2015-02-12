# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import (current_app as app, request, redirect, url_for, views,
                   render_template)
from ..commons import utilities
from . import forms


class Main(views.MethodView):
    """Return the Main view of the application."""

    template = 'pages/main.html'
    form_class = forms.RunForm

    def get_data(self, **kwargs):
        return {
            'form': self.form_class(),
            'report': False
        }

    def get(self, **kwargs):
        return render_template(self.template, **self.get_data(**kwargs))

    def post(self, **kwargs):
        data = self.get_data(**kwargs)
        payload = utilities.clean_payload(utilities.get_runargs())
        generate_report = utilities.get_reporturl(payload)

        if data['form'].validate_on_submit():
            pipeline = utilities.get_pipeline(pipeline_args)
            if pipeline is None:
                data['report'] = app.config['TVWEB_PIPELINE_BUILD_ERROR_RESPONSE']
            else:
                success, report = pipeline.run()
                data.update({'success': success, 'report': report, 'generate_report': generate_report})

        return render_template(self.template, **data)
