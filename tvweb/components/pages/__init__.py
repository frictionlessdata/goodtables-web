from flask import Blueprint
from . import views


blueprint = Blueprint('pages', __name__, url_prefix='')


blueprint.add_url_rule('/', view_func=views.Main.as_view('main'))
