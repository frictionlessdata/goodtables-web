import os
import json
from table_validation import factory
from table_validation.config import default


app = factory.create_app(default)


if app.config['DEBUG']:
    app.debug = True


if __name__ == '__main__':
    app.run()
