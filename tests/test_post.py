# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import io
import json
from tests import base
from tvweb import compat


class TestAPIPost(base.BaseTestCase):

    def test_post_valid_url_upload(self):
        data = {'data': '{0}/valid.csv'.format(self.http_data)}
        resp = self._post('api.run', data, with_files=False)
        data = json.loads(compat.str(resp.data, encoding='utf-8'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(data['success'])

    def test_post_invalid_url_upload(self):
        data = {'data': '{0}/defective_rows.csv'.format(self.http_data)}
        resp = self._post('api.run', data, with_files=False)
        data = json.loads(compat.str(resp.data, encoding='utf-8'))
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(data['success'])

    def test_post_valid_file_upload(self):
        with io.open(os.path.join(self.local_data, 'valid.csv'), 'r+b') as stream:
            data = {'data': (stream, 'file.csv')}
            resp = self._post('api.run', data, with_files=True)
            data = json.loads(compat.str(resp.data, encoding='utf-8'))
            self.assertTrue(data['success'])

    def test_post_invalid_file_upload(self):
        with io.open(os.path.join(self.local_data, 'invalid.csv'), 'r+b') as stream:
            data = {'data': (stream, 'file.csv')}
            resp = self._post('api.run', data, with_files=True)
            data = json.loads(compat.str(resp.data, encoding='utf-8'))
            self.assertFalse(data['success'])

    def test_row_limit_param_over_api(self):
        with io.open(os.path.join(self.local_data, 'invalid.csv'), 'r+b') as stream:
            data = {'data': (stream, 'file.csv'), 'row_limit': '1'}
            resp = self._post('api.run', data)
            data = json.loads(compat.str(resp.data, encoding='utf-8'))
            self.assertFalse(data['success'])
            self.assertTrue(len(data['report']['structure']['results']) <= 1)

    def test_report_limit_param_over_api(self):
        with io.open(os.path.join(self.local_data, 'invalid.csv'), 'r+b') as stream:
            data = {'data': (stream, 'file.csv'), 'report_limit': '1'}
            resp = self._post('api.run', data)
            data = json.loads(compat.str(resp.data, encoding='utf-8'))
            self.assertFalse(data['success'])
