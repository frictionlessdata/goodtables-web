from flask import Blueprint
from . import views


blueprint = Blueprint('api', __name__, url_prefix='/api')


blueprint.add_url_rule('/', view_func=views.Index.as_view('index'))
blueprint.add_url_rule('/submit', view_func=views.Submit.as_view('submit'))
# blueprint.add_url_rule('/jobs', view_func=views.JobList.as_view('jobs'))
# blueprint.add_url_rule('/jobs/<lookup>', view_func=views.Auth.as_view('job'))
