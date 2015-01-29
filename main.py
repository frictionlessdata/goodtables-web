# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from tvweb import factory
from tvweb.config import default


app = factory.create_app(default)


if app.config['DEBUG']:
    app.debug = True


if __name__ == '__main__':
    app.run()
