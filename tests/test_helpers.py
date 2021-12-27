import allure
import pytest

from tests.helpers import url_path_for


@allure.feature('Утилиты')
@allure.story('Тестирование внутренних утилит')
@allure.label('layer', 'unit')
@pytest.mark.parametrize(
    'name,query_params,path_params,expected',
    [
        ('get_list_of_shares', {}, {}, '/api/shares/'),
        ('get_list_of_shares', {'limit': 10}, {}, '/api/shares/?limit=10'),
        ('get_share', {}, {'ticker': 'TSLA'}, '/api/shares/TSLA/'),
        ('get_share', {'limit': 10}, {'ticker': 'TSLA'}, '/api/shares/TSLA/?limit=10'),
    ],
)
def test_url_path_for(name, query_params, path_params, expected):
    assert url_path_for(name, query_params=query_params, **path_params) == expected
