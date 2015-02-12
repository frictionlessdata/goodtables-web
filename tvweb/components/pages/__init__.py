# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import Blueprint
from . import views


blueprint = Blueprint('pages', __name__, url_prefix='')


blueprint.add_url_rule('/', view_func=views.Main.as_view('main'))
