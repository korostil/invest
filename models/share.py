from pydantic import BaseModel, Field


class Share(BaseModel):
    ticker: str = Field(...)

    class Config:
        schema_extra = {'example': {'ticker': 'TSLA'}}
