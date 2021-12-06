import uvicorn
from fastapi import FastAPI

from api import router
from app.settings import settings

app = FastAPI(title=settings.app_name, debug=settings.debug)
app.include_router(router, prefix='/api')


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.app_host,
        port=settings.app_port,
        debug=settings.debug,
        reload=settings.debug,
    )
