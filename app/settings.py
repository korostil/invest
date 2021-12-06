from pydantic import BaseSettings, ValidationError


class Settings(BaseSettings):
    # App
    app_name: str = 'invest'
    app_host: str = '0.0.0.0'
    app_port: int = 8000
    debug: bool = False

    # Database
    mongodb_host: str = 'localhost'
    mongodb_port: int = 27017
    mongodb_database: str = 'invest'


try:
    settings = Settings()
except ValidationError:
    # TODO log error
    raise SystemExit(1)
