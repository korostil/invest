from typing import Generator

from app.database import database


def get_db() -> Generator:
    yield database
