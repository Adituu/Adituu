import flask
import datetime

blueprint = flask.Blueprint(name='index', import_name=__name__)


@blueprint.get('/')
def index():
    current_year = datetime.datetime.now().year

    render_args = {
        'year': current_year
    }

    return flask.render_template('index.html', **render_args), 200
