import flask

from flaskr.core.utils import (
    get_current_year
)

blueprint = flask.Blueprint(name='index', import_name=__name__)


@blueprint.get('/')
def index():
    render_args = {
        'year': get_current_year()
    }

    return flask.render_template('index.html', **render_args), 200
