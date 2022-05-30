import flask

blueprint = flask.Blueprint(name='robots', import_name=__name__)


@blueprint.get('/robots.txt')
def robots():
    return flask.redirect(flask.url_for('static', filename='robots.txt'), 302)
