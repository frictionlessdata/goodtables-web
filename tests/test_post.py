# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# import os
# import io
import json
from tests import base


class TestAPIPost(base.BaseTestCase):

    def test_post_valid_url_upload(self):
        data = {'data_source': '{0}/valid.csv'.format(self.http_data)}
        resp = self._post('api.run', data, with_files=False)
        data = json.loads(str(resp.data, encoding='utf-8'))

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(data['success'])

    def test_post_invalid_url_upload(self):
        data = {'data_source': '{0}/defective_rows.csv'.format(self.http_data)}
        resp = self._post('api.run', data, with_files=False)
        data = json.loads(str(resp.data, encoding='utf-8'))

        self.assertEqual(resp.status_code, 200)
        self.assertFalse(data['success'])

    # def test_post_valid_file_upload(self):
    #     with io.open(os.path.join(self.local_data, 'valid.csv'), 'r+b') as f:
    #         data = {'data_source': '{0}/valid.csv'.format(self.http_data),
    #                 'file': (f, 'a_file_name.csv')}
    #         resp = self._post('api.run', data, with_files=True)
    #
    #         self.assertTrue(False)
    #
    # def test_post_invalid_file_upload(self):
    #     data = {'data_source': '{0}/valid.csv'.format(self.http_data)}
    #     resp = self._post('api.run', data, with_files=False)
    #
    #     self.assertTrue(False)
