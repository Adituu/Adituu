import flask
import logging
import sys

from flaskr.core.utils import (
    get_current_year
)

logger = logging.getLogger('flaskr.errors')
logger.setLevel(logging.INFO)

logger_handler = logging.StreamHandler(sys.stdout)
logger_handler.setLevel(logging.INFO)

logger_format = logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s - %(message)s')
logger_handler.setFormatter(logger_format)

logger.addHandler(logger_handler)


def http_exception_error(error):
    logger.error(error)

    render_args = {
        'year': get_current_year(),
        'error_code': error.code if error.code else 500,
        'error_message': error.__cause__ if error.__cause__ else 'Http exception error'
    }

    return flask.render_template('error.html', **render_args), error.code if error.code else 500


def internal_error(error):
    logger.error(error)

    render_args = {
        'year': get_current_year(),
        'error_code': 500,
        'error_message': error.__cause__ if error.__cause__ else 'Internal error'
    }

    return flask.render_template('error.html', **render_args), 500


def not_found_error(error):
    logger.error(error)

    render_args = {
        'year': get_current_year(),
        'error_code': 404,
        'error_message': error.__cause__ if error.__cause__ else 'Not found'
    }

    return flask.render_template('error.html', **render_args), 404
