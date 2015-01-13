import os
import json
from tabular_validator_web import factory
from tabular_validator_web.config import default


app = factory.create_app(default)


if app.config['DEBUG']:
    app.debug = True


if __name__ == '__main__':
    app.run()
