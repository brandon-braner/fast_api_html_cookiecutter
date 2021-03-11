import os
import pathlib
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings

app_path = pathlib.Path().absolute()


class Settings(BaseSettings):
    app_name: str = "{{cookiecutter.app_name}}"
    mongo_db: str = os.getenv("MONGODB_NAME", '{{cookiecutter.app_name}}')
    mongo_username = os.getenv("MONGO_USERNAME", 'root')
    mongo_password = os.getenv("MONGO_PASSWORD", 'passowrd')
    mongo_host = os.getenv("MONGO_HOST", "127.0.0.1")

    class Config:
        env_prefix = '{{cookiecutter.env_prefix}}_'  # Prefix env variables with this to replace the definition above


def load_environment_files():
    environment = os.getenv('environment') if os.getenv('environment') else 'development'
    common_env = Path(app_path) / 'common.env'
    environment_env = Path(app_path) / f'{environment}.env'
    return [common_env, environment_env]


def get_settings():
    common_env, environment_env = load_environment_files()

    load_dotenv(dotenv_path=common_env)
    load_dotenv(dotenv_path=environment_env, override=True)
    return Settings()
