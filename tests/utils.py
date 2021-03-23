import urllib.parse

from app import app


def url_path_for(name: str, query_params: dict = None, **path_params: str) -> str:
    url: str = app.url_path_for(name, **path_params)
    if query_params:
        url += '?' + urllib.parse.urlencode(query_params)
    return url
