import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.mark.asyncio
@pytest.fixture(autouse=True)
async def test_database(event_loop) -> AsyncGenerator:
    from app.database import client

    yield
    await client.drop_database('test_invest')


@pytest.mark.asyncio
@pytest.fixture
async def client() -> AsyncGenerator:
    from main import app

    client = AsyncClient(app=app, base_url='http://localhost')
    yield client
    await client.aclose()
