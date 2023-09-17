import flask

from werkzeug.middleware.proxy_fix import ProxyFix

from werkzeug.exceptions import (
    HTTPException,
    InternalServerError
)

from flaskr.core.settings import settings

from flaskr.routes import (
    index,
    robots,
    projects,
    shorten
)

from flaskr.core.errors import (
    http_exception_error,
    internal_error
)


def create_app():
    app = flask.Flask(__name__, static_folder='templates/static')

    # Flask core settings
    app.config['ENV'] = settings.FLASK_ENVIRONMENT
    app.config['SECRET_KEY'] = settings.FLASK_SECRET
    app.config['JSON_SORT_KEYS'] = False

    # Proxy fix
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

    # Blueprints
    app.register_blueprint(index.blueprint)
    app.register_blueprint(robots.blueprint)
    app.register_blueprint(projects.blueprint)
    app.register_blueprint(shorten.blueprint)

    # Error handlers
    app.register_error_handler(HTTPException, http_exception_error)
    app.register_error_handler(InternalServerError, internal_error)
    app.register_error_handler(Exception, internal_error)

    return app
