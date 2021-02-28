import re
from typing import Any, Dict, List

from pydantic import BaseModel, Field, condecimal, validator
from pydantic.types import Decimal  # noqa


class Company(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    industry: str = Field(...)
    ratios: List[Dict[str, Any]]
    financial_statements: List[Dict[str, Any]]


class Ratio(BaseModel):
    title: str = Field(...)
    quarter: str = Field(...)  # ex.: 2020Q3
    value: condecimal(decimal_places=2)  # type: ignore

    @validator('quarter')
    def quarter_validator(cls, value):
        if not re.match(r"^\d{4}Q[1-4]$", value):
            raise ValueError(
                "quarter must match pattern <year>Q<quarter_number> (ex.:2020Q3)"
            )
        return value


class FinancialStatement(BaseModel):
    title: str = Field(...)
    quarter: str = Field(...)  # ex.: 2020Q3
    value: condecimal(decimal_places=2)  # type: ignore

    @validator('quarter')
    def quarter_validator(cls, value):
        if not re.match(r"^\d{4}Q[1-4]$", value):
            raise ValueError(
                "quarter must match pattern <year>Q<quarter_number> (ex.:2020Q3)"
            )
        return value
