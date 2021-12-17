from typing import Any

import allure
import pytest
from fastapi import status
from httpx import AsyncClient

from tests.factories.share import ShareFactory
from tests.helpers import (
    serialize_share,
    serialize_shares,
    serializer_api_response,
    url_path_for,
)

pytestmark = [pytest.mark.asyncio]


@allure.feature('Акции')
@allure.story('Получение списка акций')
@allure.label('layer', 'API')
class GetSharesListTestCase:
    @allure.title('При указании некорректного limit вернется ошибка')
    @pytest.mark.parametrize('value', [-1, 0, 'a', 101])
    async def test_invalid_limit(self, client: AsyncClient, value: Any):
        response = await client.get(
            url_path_for('get_list_of_shares', query_params={'limit': value})
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    @allure.title('При указании некорректного offset вернется ошибка')
    @pytest.mark.parametrize('value', [-1, 'a'])
    async def test_invalid_offset(self, client: AsyncClient, value: Any):
        response = await client.get(
            url_path_for('get_list_of_shares', query_params={'offset': value})
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    @allure.title('Если акций нет, то вернется пустой список')
    async def test_empty(self, client: AsyncClient):
        response = await client.get(url_path_for('get_list_of_shares'))

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == serializer_api_response()

    @allure.title(
        'Если offset превышает общее количество акций, то вернется пустой список'
    )
    async def test_offset_gt_total(self, client: AsyncClient):
        response = await client.get(url_path_for('get_list_of_shares'))

        assert response.status_code == status.HTTP_200_OK

    @allure.title('Если переданы limit и offset, то акции отдаются постранично')
    @pytest.mark.parametrize('limit,offset,total', [(1, 0, 2), (1, 1, 2)])
    async def test_pagination(
        self, client: AsyncClient, limit: int, offset: int, total: int
    ):
        shares = await ShareFactory.create_batch(size=total)
        response = await client.get(
            url_path_for(
                'get_list_of_shares', query_params={'limit': limit, 'offset': offset}
            )
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == serializer_api_response(
            serialize_shares(shares[offset])
        )


@allure.feature('Акции')
@allure.story('Получение конкретной акций')
@allure.label('layer', 'API')
class GetShareTestCase:
    @allure.title('Если запрошенной акции нет, то вернется ошибка')
    async def test_not_found(self, client: AsyncClient):
        response = await client.get(url_path_for('get_share', ticker='TSLA'))

        assert response.status_code == status.HTTP_404_NOT_FOUND

    @allure.title('Если запрошенная акция есть, то вернутся данные об акции')
    async def test_success(self, client: AsyncClient):
        ticker = 'TSLA'
        share = await ShareFactory.create(ticker=ticker)

        response = await client.get(url_path_for('get_share', ticker=ticker))

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == serializer_api_response(serialize_share(share))
