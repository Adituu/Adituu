from gevent.pywsgi import WSGIServer

from flaskr import create_app

from flaskr.core.settings import settings

http_server = WSGIServer((settings.HTTP_SERVER_HOST, int(settings.HTTP_SERVER_PORT)),
                         log=None if settings.FLASK_ENVIRONMENT == 'production' else 'default', application=create_app())
http_server.serve_forever()
