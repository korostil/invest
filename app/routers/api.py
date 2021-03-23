from fastapi import APIRouter

router = APIRouter()


@router.get("/share/", tags=["shares"])
async def get_share_list(limit: int = 20, offset: int = 0):
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/share/{ticker}/", tags=["shares"])
async def get_share(ticker: str):
    return [{"username": "Rick"}, {"username": "Morty"}]
