import flask

blueprint = flask.Blueprint(name='robots', import_name=__name__)


@blueprint.route('/robots.txt', methods=['GET', 'POST', 'HEAD'])
def robots():
    return flask.redirect(flask.url_for('static', filename='robots.txt'), 302)
