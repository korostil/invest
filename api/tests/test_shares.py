from http import HTTPStatus
from typing import Any

import allure
import pytest
from httpx import AsyncClient

from tests.utils import url_path_for


@allure.feature('Акций')
@allure.story('Получение списка акций')
@allure.label('layer', 'API')
class GetSharesListTestCase:
    @allure.title('При указании некорректного limit или offset вернется ошибка')
    @pytest.mark.asyncio
    @pytest.mark.parametrize('param', ['limit', 'offset'])
    @pytest.mark.parametrize('value', [-1, 'a'])
    async def test_invalid_limit_offset(
        self, client: AsyncClient, param: str, value: Any
    ):
        response = await client.get(url_path_for('get_list_of_shares'))

        assert response.status_code == HTTPStatus.BAD_REQUEST

    @allure.title('Если акций нет, то вернется пустой список')
    @pytest.mark.asyncio
    async def test_empty(self, client: AsyncClient):
        response = await client.get(url_path_for('get_list_of_shares'))

        assert response.status_code == HTTPStatus.OK
        assert response.json() == {'status': 'ok', 'data': []}

    @allure.title(
        'Если offset превышает общее количество акций, то вернется пустой список'
    )
    @pytest.mark.asyncio
    async def test_offset_gt_total(self, client: AsyncClient):
        response = await client.get(url_path_for('get_list_of_shares'))

        assert response.status_code == HTTPStatus.OK

    @allure.title('Если переданы offset+limit, то акции отдаются постранично')
    @pytest.mark.asyncio
    @pytest.mark.parametrize('limit,offset,total', [(1, 0, 2), (1, 1, 2)])
    async def test_pagination(
        self, client: AsyncClient, limit: int, offset: int, total: int
    ):
        response = await client.get(
            url_path_for(
                'get_list_of_shares', query_params={'limit': limit, 'offset': offset}
            )
        )

        assert response.status_code == HTTPStatus.OK
