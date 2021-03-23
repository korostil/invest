from fastapi import APIRouter

router = APIRouter()


@router.get("/share/", tags=["shares"])
async def get_list_of_shares(limit: int = 25, offset: int = 0):
    return {'status': 'ok', 'data': []}


@router.get("/share/{ticker}/", tags=["shares"])
async def get_share_info(ticker: str):
    return [{"username": "Rick"}, {"username": "Morty"}]
