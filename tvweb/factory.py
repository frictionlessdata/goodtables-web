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
    from .components import core, api
    from .components.commons import context_processors, encoders

    # Construct the app object
    app = Flask('tvweb', static_url_path='/static')

    # Configure the app with the default configuration
    app.config.from_object(config)

    # Initialize core services on the app object
    core.api.init_app(app)

    # Set custom context processors
    app.context_processor(context_processors.inject_app_data)

    # Set custom encoders
    app.json_encoder = encoders.JSONEncoder

    return app
