from pydantic import BaseModel, Field


class ShareResponse(BaseModel):
    ticker: str = Field(...)

    class Config:
        schema_extra = {'example': {'ticker': 'TSLA'}}


class ShareCreate(BaseModel):
    ticker: str = Field(...)


class ShareUpdate(BaseModel):
    ticker: str = Field(...)
