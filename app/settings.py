from pydantic import BaseSettings, ValidationError


class Settings(BaseSettings):
    # Database
    mongodb_host = 'localhost'
    mongodb_port = 27017
    mongodb_database = 'invest'


try:
    settings = Settings()
except ValidationError:
    # TODO log error
    raise SystemExit(1)
