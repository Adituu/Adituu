import loguru

from gevent.pywsgi import WSGIServer

from flaskr import create_app
from flaskr.core.settings import settings


def main() -> None:
    loguru.logger.add(
        sink='./log/error.log', level='ERROR')
    loguru.logger.add(
        sink='./log/info.log', filter=lambda record: record['level'].name not in ('ERROR', 'CRITICAL'), level='INFO')

    http_server = WSGIServer((settings.HTTP_SERVER_HOST, int(settings.HTTP_SERVER_PORT)),
                             log=None if settings.FLASK_ENVIRONMENT == 'production' else 'default', application=create_app())
    http_server.serve_forever()


if __name__ == '__main__':
    main()
