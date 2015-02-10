# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import Blueprint
from flask.ext import restful
from . import views


blueprint = Blueprint('api', __name__)
api = restful.Api(blueprint)
api.add_resource(views.Main, '/api', endpoint='main')
api.add_resource(views.Run, '/api/run', endpoint='run')
