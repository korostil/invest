import allure
import pytest

from tests.helpers import url_path_for


@allure.feature('Утилиты')
@allure.story('Тестирование внутренних утилит')
@allure.label('layer', 'unit')
@pytest.mark.parametrize(
    'name,query_params,path_params,expected',
    [
        ('get_list_of_shares', {}, {}, '/api/share/'),
        ('get_list_of_shares', {'limit': 10}, {}, '/api/share/?limit=10'),
        ('get_share_info', {}, {'ticker': 'TSLA'}, '/api/share/TSLA/'),
        (
            'get_share_info',
            {'limit': 10},
            {'ticker': 'TSLA'},
            '/api/share/TSLA/?limit=10',
        ),
    ],
)
def test_url_path_for(name, query_params, path_params, expected):
    assert url_path_for(name, query_params=query_params, **path_params) == expected
