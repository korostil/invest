import pytest
from httpx import AsyncClient

from app import app


@pytest.mark.asyncio
@pytest.fixture
def client():
    return AsyncClient(app=app, base_url='http://localhost')
