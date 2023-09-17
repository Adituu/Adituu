from fastapi import FastAPI

from application.core.config.app import app_config
from application.core.config.database import database_config
from application.core.database import db


def create_app() -> FastAPI:
    app = FastAPI(
        debug=app_config.FASTAPI_DEBUG_MODE,
        title=app_config.FASTAPI_NAME,
        version=app_config.PACKAGE_VERSION,
        redoc_url=app_config.FASTAPI_REDOC_PATH,
        swagger_ui_parameters={'defaultModelsExpandDepth': -1}
    )

    db.init_db(database_config.MONGODB_URL)

    return app
