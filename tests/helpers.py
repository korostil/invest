import urllib.parse
from typing import Optional, Union

from funcy import collecting

from main import app
from models.share import Share


def url_path_for(name: str, query_params: dict = None, **path_params: str) -> str:
    url: str = app.url_path_for(name, **path_params)
    if query_params:
        url += '?' + urllib.parse.urlencode(query_params)
    return url


def serializer_api_response(data: Optional[Union[dict, list]] = None) -> dict:
    data = data or []
    response = {'status': 'ok', 'data': data}

    if isinstance(data, list):
        response['count'] = len(data)

    return response


@collecting
def serialize_shares(*shares):
    for share in shares:
        yield serialize_share(share)


def serialize_share(share: Share, **extra) -> dict:
    return {'ticker': share.ticker}
