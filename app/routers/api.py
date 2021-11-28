from fastapi import APIRouter, Query

from app.database import database
from models.share import Share

router = APIRouter()


@router.get("/share/", tags=["shares"])
async def get_list_of_shares(
    limit: int = Query(25, gt=0, le=100), offset: int = Query(0, ge=0)
) -> dict:
    shares = database.shares.find(skip=offset)
    return {
        'status': 'ok',
        'data': [Share(**share) for share in await shares.to_list(limit)],
    }


@router.get("/share/{ticker}/", tags=["shares"])
async def get_share_info(ticker: str) -> list:
    return [{"username": "Rick"}, {"username": "Morty"}]
