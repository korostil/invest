from http import HTTPStatus
from typing import Any

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from funcy import is_seqcont
from starlette.responses import JSONResponse

from utils import dumps

__all__ = (
    'APIResponse',
    'BadRequest',
    'NotFound',
    'RequestEntityTooLarge',
    'ServiceUnavailable',
    'UnprocessableEntity',
)


class APIResponse(JSONResponse):
    media_type = 'application/json'

    def render(self, content: Any) -> Any:
        if is_seqcont(content):
            data: list = list(content)
            content = {'status': 'ok', 'data': data, 'count': len(data)}
        else:
            content = {'status': 'ok', 'data': content}

        return dumps(jsonable_encoder(content)).encode('utf-8')


class CustomHTTPException(HTTPException):
    status: HTTPStatus

    def __init__(self, message: str = ''):
        super().__init__(
            status_code=self.status.value, detail=message or self.status.phrase
        )


class BadRequest(CustomHTTPException):
    status = HTTPStatus.BAD_REQUEST


class RequestEntityTooLarge(CustomHTTPException):
    status = HTTPStatus.REQUEST_ENTITY_TOO_LARGE


class UnprocessableEntity(CustomHTTPException):
    status = HTTPStatus.UNPROCESSABLE_ENTITY


class NotFound(CustomHTTPException):
    status = HTTPStatus.NOT_FOUND


class ServiceUnavailable(CustomHTTPException):
    status = HTTPStatus.SERVICE_UNAVAILABLE


class Unauthorized(CustomHTTPException):
    status = HTTPStatus.UNAUTHORIZED
