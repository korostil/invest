from typing import Any

import allure
import pytest
from fastapi import status
from httpx import AsyncClient

from tests.factories.share import ShareDocumentFactory, ShareFactory
from tests.helpers import (
    serialize_share,
    serialize_shares,
    serializer_api_response,
    url_path_for,
)

pytestmark = [pytest.mark.asyncio]


@allure.feature('Shares')
@allure.story('Get share list')
@allure.label('layer', 'API')
class GetSharesListTestCase:
    @allure.title('If an invalid limit submitted, an error will be returned')
    @pytest.mark.parametrize('value', [-1, 0, 'a', 101])
    async def test_invalid_limit(self, client: AsyncClient, value: Any):
        response = await client.get(
            url_path_for('get_list_of_shares', query_params={'limit': value})
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    @allure.title('If an invalid offset submitted, an error will be returned')
    @pytest.mark.parametrize('value', [-1, 'a'])
    async def test_invalid_offset(self, client: AsyncClient, value: Any):
        response = await client.get(
            url_path_for('get_list_of_shares', query_params={'offset': value})
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    @allure.title('If there are no shares, returns an empty list')
    async def test_empty(self, client: AsyncClient):
        response = await client.get(url_path_for('get_list_of_shares'))

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == serializer_api_response()

    @allure.title('If an offset is greater than shares number, returns an empty list')
    async def test_offset_gt_total(self, client: AsyncClient):
        response = await client.get(url_path_for('get_list_of_shares'))

        assert response.status_code == status.HTTP_200_OK

    @allure.title('Shares successfully paginated by limit and offset')
    @pytest.mark.parametrize('limit,offset,total', [(1, 0, 2), (1, 1, 2)])
    async def test_pagination(
        self, client: AsyncClient, limit: int, offset: int, total: int
    ):
        shares = await ShareDocumentFactory.create_batch(size=total)
        response = await client.get(
            url_path_for(
                'get_list_of_shares', query_params={'limit': limit, 'offset': offset}
            )
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == serializer_api_response(
            serialize_shares(shares[offset])
        )


@allure.feature('Shares')
@allure.story('Get a share info')
@allure.label('layer', 'API')
class GetShareTestCase:
    @allure.title('If there is no requested share, an error will be returned')
    async def test_not_found(self, client: AsyncClient):
        response = await client.get(url_path_for('get_share', ticker='TSLA'))

        assert response.status_code == status.HTTP_404_NOT_FOUND

    @allure.title('Share successfully received')
    async def test_success_get(self, client: AsyncClient):
        ticker = 'TSLA'
        share = await ShareDocumentFactory.create(ticker=ticker)

        response = await client.get(url_path_for('get_share', ticker=ticker))

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == serializer_api_response(serialize_share(share))


@allure.feature('Shares')
@allure.story('Create a share')
@allure.label('layer', 'API')
class CreateShareTestCase:
    @allure.title('If ticker is not submitted, an error will be returned')
    async def test_ticker_required(self, client: AsyncClient):
        response = await client.post(url_path_for('create_share'), json={})

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    @allure.title('If a non-unique ticker is submitted, an error will be returned')
    async def test_not_unique_ticker(self, client: AsyncClient):
        ticker = 'TSLA'
        await ShareDocumentFactory.create(ticker=ticker)
        share = ShareFactory.create(ticker=ticker)

        response = await client.post(url_path_for('create_share'), json=share.dict())

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    @allure.title('Share successfully created')
    async def test_success_create(self, client: AsyncClient):
        share = ShareFactory.create()

        response = await client.post(url_path_for('create_share'), json=share.dict())

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == serializer_api_response(serialize_share(share))
