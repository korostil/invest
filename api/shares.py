import funcy
from fastapi import APIRouter, Query
from marshmallow import ValidationError

from app.responses import APIResponse, NotFound, UnprocessableEntity
from schemas.share import ShareCreate, ShareResponse
from services.shares import share

router = APIRouter()


@router.get('/shares/', tags=['shares'])
async def get_list_of_shares(
    limit: int = Query(25, gt=0, le=100), offset: int = Query(0, ge=0)
) -> APIResponse:
    shares = await share.get_list(limit=limit, skip=offset)
    return APIResponse(
        [
            ShareResponse(**share_document)
            for share_document in funcy.lmap(lambda x: x.dump(), shares)
        ]
    )


@router.get('/shares/{ticker}/', tags=['shares'])
async def get_share(ticker: str = Query(...)) -> APIResponse:
    share_document = await share.get(ticker)
    if not share_document:
        raise NotFound
    return APIResponse(ShareResponse(**share_document.dump()))


@router.post('/shares/', tags=['shares'])
async def create_share(share_data: ShareCreate) -> APIResponse:
    with funcy.reraise(ValidationError, UnprocessableEntity):
        share_document = await share.create(document=share_data)

    return APIResponse(ShareResponse(**share_document.dump()))
