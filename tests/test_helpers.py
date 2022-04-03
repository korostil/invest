import allure
import pytest

from tests.helpers import url_path_for
from utils import get_latest_api_version

VERSION = get_latest_api_version()


@allure.feature('Internal utilities')
@allure.story('Test helpers')
@allure.label('layer', 'unit')
@allure.title('Get an url of view')
@pytest.mark.parametrize(
    'name,query_params,path_params,expected',
    [
        ('get_list_of_shares', {}, {}, f'/api/{VERSION}/shares/'),
        ('get_list_of_shares', {'limit': 10}, {}, f'/api/{VERSION}/shares/?limit=10'),
        ('get_share', {}, {'ticker': 'TSLA'}, f'/api/{VERSION}/shares/TSLA/'),
        (
            'get_share',
            {'limit': 10},
            {'ticker': 'TSLA'},
            f'/api/{VERSION}/shares/TSLA/?limit=10',
        ),
    ],
)
def test_url_path_for(name, query_params, path_params, expected):
    assert url_path_for(name, query_params=query_params, **path_params) == expected
