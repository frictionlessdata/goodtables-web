# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import unittest
from flask import url_for
from tvweb import factory
from tvweb.config import test as test_config


class BaseTestCase(unittest.TestCase):

    """Common stuff for tests."""

    http_data = ('https://raw.githubusercontent.com/okfn/'
                 'tabular-validator/master/examples/')
    local_data = os.path.abspath(os.path.join(
        os.path.dirname(os.path.dirname(__file__)), 'examples'))

    @property
    def app(self):
        """Return an application instance for use in tests."""

        return factory.create_app(test_config)

    def run(self, result=None):
        """Run tests with appropriate Flask contexts."""

        with self.app.app_context(), self.app.test_request_context():
            self.client = self.app.test_client()
            super(BaseTestCase, self).run(result)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _get(self, route_name, **route_kwargs):
        """Factory for creating client get requests."""

        if route_kwargs:
            url = url_for(route_name, **route_kwargs)

        else:
            url = url_for(route_name)

        return self.client.get(url)

    def _post(self, route_name, data, with_files=True, **route_kwargs):
        """Factory for creating client post requests."""

        if with_files:
            mtype = 'multipart/form-data'
        else:
            mtype = 'application/x-www-form-urlencoded'

        headers = {'Content-type': mtype}

        if route_kwargs:
            url = url_for(route_name, **route_kwargs)

        else:
            url = url_for(route_name)

        return self.client.post(url, data=data, headers=headers,
                                follow_redirects=True)
