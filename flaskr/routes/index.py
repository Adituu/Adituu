import flask
import datetime

blueprint = flask.Blueprint(name='index', import_name=__name__)


@blueprint.get('/')
def index():
    current_year = datetime.datetime.now().year
    return flask.render_template('index.html', copyright_year=f'2022-{current_year}'), 200
