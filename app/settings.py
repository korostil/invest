from pydantic import BaseSettings


class Settings(BaseSettings):
    # Database
    mongodb_host = 'localhost'
    mongodb_port = 27017
