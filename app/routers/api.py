from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/share/", tags=["shares"])
async def get_list_of_shares(
    limit: int = Query(25, gt=0, le=100), offset: int = Query(0, ge=0)
):
    return {'status': 'ok', 'data': []}


@router.get("/share/{ticker}/", tags=["shares"])
async def get_share_info(ticker: str):
    return [{"username": "Rick"}, {"username": "Morty"}]
