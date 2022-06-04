import flask
import os

blueprint = flask.Blueprint(name='projects', import_name=__name__,
                            template_folder='../projects', static_folder='../projects/static',
                            static_url_path='/projects_static')


@blueprint.get('/projects/<project_name>')
def projects(project_name: str):
    if project_name not in os.listdir('./flaskr/projects'):
        return flask.render_template('error.html', error_code=400, error_message='Invalid project id'), 400

    return flask.render_template(f'{project_name}/index.html', project_name=project_name), 200
