import pytest
from httpx import AsyncClient

from app import app


@pytest.mark.asyncio
@pytest.fixture
async def client():
    client = AsyncClient(app=app, base_url='http://localhost')
    yield client
    await client.aclose()
