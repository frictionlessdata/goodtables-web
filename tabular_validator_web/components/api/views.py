from flask import current_app as app
from ..commons import views


class Index(views.APIView):

    """Returns a detail view for a given Account."""

    def data(self, **kwargs):
        data = super(Index, self).data(**kwargs)
        return data

    # def post(self, data, **kwargs):
    #     return True


class Submit(views.APIView):

    """Returns a detail view for a given Account."""

    def data(self, **kwargs):
        data = super(Submit, self).data(**kwargs)
        return data

    # def post(self, data, **kwargs):
    #     return True
