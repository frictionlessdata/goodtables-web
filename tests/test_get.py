# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import io
import json
from tests import base
from web import compat


class TestAPIGet(base.BaseTestCase):

    def test_get_valid_url_upload(self):
        data = {'data': '{0}/valid.csv'.format(self.http_data)}
        resp = self._get('api.run', data)
        data = json.loads(compat.str(resp.data, encoding='utf-8'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(data['success'])
