import flask

blueprint = flask.Blueprint(name='index', import_name=__name__)


@blueprint.get('/')
def index():
    return flask.render_template('index.html'), 200
