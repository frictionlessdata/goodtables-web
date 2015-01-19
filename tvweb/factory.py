def create_app(config):

    """A factory that returns an application object from the passed config.

    The factory accepts further configuration from ENV variables. Some simple
    checks for core configuration settings are made to raise errors early
    if vital information is missing.

    """

    import os
    from flask import Flask
    from .components import api
    from .components.commons import context_processors, encoders

    # Construct the app object
    app = Flask('tvweb', static_url_path='/static')

    # Configure the app with the default configuration
    app.config.from_object(config)

    # Initialize core services on the app object
    # core.trans.init_app(app)

    # Register routable app components as blueprints on the app
    app.register_blueprint(api.blueprint)

    # Set additional jinja2 extensions
    # app.jinja_env.add_extension('jinja2.ext.do')

    # Set custom context processors
    # app.context_processor(context_processors.inject_app_data)

    # Set custom encoders
    app.json_encoder = encoders.JSONEncoder

    return app
