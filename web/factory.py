# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


def create_app(config):

    """A factory that returns an application object from the passed config.

    The factory accepts further configuration from ENV variables. Some simple
    checks for core configuration settings are made to raise errors early
    if vital information is missing.

    """

    import os
    from flask import Flask
    from flask.ext.babel import Babel
    from flask.ext.cors import CORS
    from flask.ext.markdown import Markdown
#    from flask.ext.assets import Environment, Bundle
    from .components import api, pages
    from .components.commons import context_processors, encoders

    app_label = 'web'

    # Get the static and template folder for the passed theme
    static_folder = os.path.join('theme', 'static')
    template_folder = os.path.join('theme', 'templates')

    # Construct app and service objects
    app = Flask(app_label, template_folder=template_folder,
                static_folder=static_folder, static_url_path='/static')
    trans = Babel()
    cors = CORS(resources=r'/api/*', allow_headers='Content-Type')
#    assets = Environment()

    # Configure the app with defaults
    app.config.from_object(config)

    # Set app core services
    trans.init_app(app)
    cors.init_app(app)
#    assets.init_app(app)
    Markdown(app)

    # Register routable components
    app.register_blueprint(api.blueprint)
    app.register_blueprint(pages.blueprint)

    # Set additional jinja2 extensions
    app.jinja_env.add_extension('jinja2.ext.do')

    # Set custom context processors
    app.context_processor(context_processors.inject_app_data)

    # Set custom encoders
    app.json_encoder = encoders.JSONEncoder

    # Register webassets bundles
#    sass = Bundle('css/base.scss', filters='pyscss', output='css/base.css')
#    assets.register('sass', sass)

    return app
