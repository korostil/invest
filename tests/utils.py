import urllib.parse

from funcy import collecting

from app import app
from models.share import Share


def url_path_for(name: str, query_params: dict = None, **path_params: str) -> str:
    url: str = app.url_path_for(name, **path_params)
    if query_params:
        url += '?' + urllib.parse.urlencode(query_params)
    return url


def serializer_api_response(data: dict) -> dict:
    return {'status': 'ok', 'data': data}


@collecting
def serialize_shares(*shares):
    for share in shares:
        yield serialize_share(share)


def serialize_share(share: Share, **extra) -> dict:
    return {'ticker': share.ticker}
