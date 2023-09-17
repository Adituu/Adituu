import flask
import loguru


def http_exception_error(error):
    loguru.logger.error(f'Http exception occured. ({error})')

    render_args = {
        'error_code': getattr(error, 'code', None) or 500,
        'error_message': getattr(error, '__cause__', None) or 'Http exception error'
    }

    return flask.render_template('error.html', **render_args), error.code if error.code else 500


def internal_error(error):
    loguru.logger.error(f'Internal exception occured. ({error})')

    render_args = {
        'error_code': 500,
        'error_message': getattr(error, '__cause__', None) or 'Internal error'
    }

    return flask.render_template('error.html', **render_args), 500
