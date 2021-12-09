import os

import fastapi
import fastapi_chameleon
import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.staticfiles import StaticFiles

from settings import Settings
from views import home

app = fastapi.FastAPI()
settings = Settings()


def main():
    configure(dev_mode=True)
    uvicorn.run(app, host='127.0.0.1', port=8080, debug=True)


def configure(dev_mode: bool):
    configure_templates(dev_mode)
    configure_routes()


def configure_templates(dev_mode: bool):
    folder = os.path.dirname(__file__)
    template_folder = os.path.join(folder, 'templates')
    template_folder = os.path.abspath(template_folder)
    fastapi_chameleon.global_init(template_folder, auto_reload=dev_mode)


def configure_db():
    username = settings.mongo_username
    password = settings.mongo_password
    client = None
    if settings.app_env == 'development':
        url = f"mongodb://{username}:{password}@localhost:27017/database_name"
        return AsyncIOMotorClient(url)
    else:
        url = f'mongodb+srv://{settings.mongo_username}:{settings.mongo_password}@{settings.mongo_host}'
        return (url)


def configure_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)


if __name__ == '__main__':
    main()
else:
    configure(dev_mode=False)
