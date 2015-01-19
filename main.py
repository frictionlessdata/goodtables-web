from tvweb import factory
from tvweb.config import default


app = factory.create_app(default)


if app.config['DEBUG']:
    app.debug = True


if __name__ == '__main__':
    app.run()
