from pydantic import BaseModel, Field


class Share(BaseModel):
    ticker: str = Field(...)
