import flask
import loguru
import json

from pathlib import Path

blueprint = flask.Blueprint(name='shorten', import_name=__name__)


@blueprint.get('/short/<short_id>')
def shorten(short_id: str):
    try:
        with open(Path.joinpath(Path.cwd(), 'shortens.json'), mode='rb') as shortens_file:
            shortens = json.load(shortens_file)

            if not shortens.get(short_id):
                return flask.render_template(
                    template_name_or_list='error.html', error_code=404, error_message='Invalid shorten link.'), 404

            else:
                return flask.redirect(shortens.get(short_id))
    except Exception as e:
        loguru.logger.error(f'Could not open \'shortens.json\'. ({e})')

        return flask.render_template(
            template_name_or_list='error.html', error_code=500, error_message='Could not open \'shortens.json\''), 400
