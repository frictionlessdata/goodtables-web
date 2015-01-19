from flask import Blueprint
from . import views


blueprint = Blueprint('api', __name__, url_prefix='/api')


blueprint.add_url_rule('/', view_func=views.Index.as_view('index'))
blueprint.add_url_rule('/jobs', view_func=views.JobList.as_view('job_list'))
blueprint.add_url_rule('/jobs/<lookup>', view_func=views.JobDetail.as_view('job_detail'))
