import os
from functools import partial

from funcy import filter, last
from ujson import dumps, loads

__all__ = ['dumps', 'loads', 'get_latest_api_version']

dumps = partial(dumps, ensure_ascii=False)


def get_latest_api_version() -> str:
    api_dir = f'{os.getcwd()}/api/'
    available_versions = filter(lambda x: x.startswith('v'), os.listdir(api_dir))
    latest_version: str = last(
        sorted(available_versions, key=lambda x: int(x.replace('v', '')))
    )
    return latest_version
