from fastapi import APIRouter, Depends, Query
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.deps import get_db
from app.responses import APIResponse, NotFound
from schemas.share import ShareResponse
from services.shares import share

router = APIRouter()


@router.get('/share/', tags=['shares'])
async def get_list_of_shares(
    limit: int = Query(25, gt=0, le=100),
    offset: int = Query(0, ge=0),
    db: AsyncIOMotorDatabase = Depends(get_db),
) -> APIResponse:
    shares = await share.get_list(db, limit=limit, skip=offset)
    return APIResponse([ShareResponse(**item) for item in shares])


@router.get('/share/{ticker}/', tags=['shares'])
async def get_share(
    ticker: str = Query(...), db: AsyncIOMotorDatabase = Depends(get_db)
) -> APIResponse:
    share_item = await share.get(db, ticker)
    if not share_item:
        raise NotFound
    return APIResponse(ShareResponse(**share_item))


@router.get('/share/{ticker}/', tags=['shares'])
async def get_share_info(ticker: str) -> list:
    return [{"username": "Rick"}, {"username": "Morty"}]
