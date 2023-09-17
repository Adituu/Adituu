import flask
import json
import loguru

from pathlib import Path

blueprint = flask.Blueprint(name='live_projects', import_name=__name__,
                            template_folder='../projects', static_folder='../projects/static',
                            static_url_path='/projects_static_folder')


@blueprint.get('/live_projects/<project_name>')
def projects(project_name: str):
    try:
        with open(Path.joinpath(Path.cwd(), 'flaskr/projects/config.projects.json'), 'r') as projects_json_config_file:
            projects_config = json.load(projects_json_config_file)
    except Exception as e:
        loguru.logger.error(f'Could not load projects json config. ({e})')

        return flask.render_template(
            template_name_or_list='error.html', error_code=500, error_message='Could not load projects json config.'), 400

    if project_name not in projects_config.values():
        return flask.render_template(
            template_name_or_list='error.html', error_code=400, error_message='Invalid project name.'), 400

    return flask.render_template(f'{project_name}/index.html', project_name=project_name), 200
