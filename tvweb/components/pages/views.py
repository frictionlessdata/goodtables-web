from flask import redirect, url_for, views, render_template


class Main(views.MethodView):
    """Return the Main view of the application."""

    template = 'pages/main.html'

#    def dispatch_request(self, **kwargs):
#        pass

    def get(self, *kwargs):
        data = {}
        return render_template(self.template, **data)

    def post(self, **kwargs):
        data = {}
        return render_template(self.template, **data)
