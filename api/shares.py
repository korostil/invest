import funcy
from fastapi import APIRouter, Query

from app.responses import APIResponse, NotFound
from schemas.share import ShareResponse
from services.shares import share

router = APIRouter()


@router.get('/share/', tags=['shares'])
async def get_list_of_shares(
    limit: int = Query(25, gt=0, le=100), offset: int = Query(0, ge=0)
) -> APIResponse:
    shares = await share.get_list(limit=limit, skip=offset)
    return APIResponse(
        [ShareResponse(**item) for item in funcy.lmap(lambda x: x.dump(), shares)]
    )


@router.get('/share/{ticker}/', tags=['shares'])
async def get_share(ticker: str = Query(...)) -> APIResponse:
    share_item = await share.get(ticker)
    if not share_item:
        raise NotFound
    return APIResponse(ShareResponse(**share_item.dump()))


@router.get('/share/{ticker}/', tags=['shares'])
async def get_share_info(ticker: str) -> list:
    return [{"username": "Rick"}, {"username": "Morty"}]
