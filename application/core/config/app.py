import dataclasses
import dotenv
import os

dotenv.load_dotenv()


@dataclasses.dataclass
class AppConfig():
    HTTP_SERVER_HOST: str = os.environ.get('HTTP_SERVER_HOST', '127.0.0.1')
    HTTP_SERVER_PORT: int = os.environ.get('HTTP_SERVER_PORT', 8080)

    FASTAPI_APP_NAME: str = os.environ.get('FASTAPI_NAME', 'test application')
    FASTAPI_DEBUG_MODE: bool = os.environ.get('FASTAPI_DEBUG_MODE', False)
    FASTAPI_REDOC_PATH: str | None = os.environ.get('FASTAPI_REDOC_PATH', None)
    # FASTAPI_UPLOAD_DIR: str | None = os.environ.get('FASTAPI_UPLOAD_DIR', None)
    # FASTAPI_OLD_UPLOAD_DIR: str | None = os.environ.get('FASTAPI_OLD_UPLOAD_DIR', None)

    ALLOWED_FILE_UPLOAD_EXTENSIONS: tuple = ('png', 'jpg', 'gif', 'jpeg', 'mp3', 'aac', 'wav', 'ogg', 'txt')


app_config = AppConfig()
