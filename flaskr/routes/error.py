import flask

blueprint = flask.Blueprint(name='error', import_name=__name__)


@blueprint.get('/error')
def error_route():
    return {
        'error': 'not found'
    }, 404
