import dataclasses
import dotenv
import os

dotenv.load_dotenv()


@dataclasses.dataclass
class Settings():
    HTTP_SERVER_HOST = os.environ.get('HTTP_SERVER_HOST', '127.0.0.1')
    HTTP_SERVER_PORT = os.environ.get('HTTP_SERVER_PORT', 80)

    FLASK_ENVIRONMENT = os.environ.get('FLASK_ENVIRONMENT', 'development')
    FLASK_SECRET = os.environ.get('FLASK_SECRET', 'dev')


settings = Settings()
