from functools import partial

from ujson import dumps, loads

dumps = partial(dumps, ensure_ascii=False)


__all__ = ['dumps', 'loads']
