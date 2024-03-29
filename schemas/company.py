import re
from typing import Any, Dict, List

from pydantic import BaseModel, Field, condecimal, constr, validator
from pydantic.types import Decimal  # noqa

from app.constants import (
    FinancialStatementCodeEnum,
    IndustryEnum,
    RatioCodeEnum,
    SectorEnum,
)


class CompanyResponse(BaseModel):
    title: constr(min_length=1)  # type: ignore
    description: str = Field('')
    industry: IndustryEnum
    sector: SectorEnum
    ratios: List[Dict[str, Any]] = Field([])
    financial_statements: List[Dict[str, Any]] = Field([])


class CompanyCreate(BaseModel):
    title: constr(min_length=1)  # type: ignore
    description: str = Field('')
    industry: IndustryEnum
    sector: SectorEnum
    ratios: List[Dict[str, Any]] = Field([])
    financial_statements: List[Dict[str, Any]] = Field([])


class CompanyUpdate(BaseModel):
    title: constr(min_length=1)  # type: ignore
    description: str = Field('')
    industry: IndustryEnum
    sector: SectorEnum
    ratios: List[Dict[str, Any]] = Field([])
    financial_statements: List[Dict[str, Any]] = Field([])


class Ratio(BaseModel):
    code: RatioCodeEnum
    quarter: str = Field(...)
    value: condecimal(decimal_places=2)  # type: ignore

    class Config:
        schema_extra = {
            'example': {'code': '1.1', 'quarter': '2020Q3', 'value': '58.32'}
        }

    @validator('quarter')
    def quarter_validator(cls, value: str) -> str:
        if not re.match(r'^\d{4}Q[1-4]$', value):
            raise ValueError(
                'quarter must match pattern <year>Q<quarter_number> (ex.:2020Q3)'
            )
        return value


class FinancialStatement(BaseModel):
    code: FinancialStatementCodeEnum
    quarter: str = Field(...)
    value: condecimal(decimal_places=2)  # type: ignore

    class Config:
        schema_extra = {
            'example': {'code': '1', 'quarter': '2020Q3', 'value': '123456789.87'}
        }

    @validator('quarter')
    def quarter_validator(cls, value: str) -> str:
        if not re.match(r'^\d{4}Q[1-4]$', value):
            raise ValueError(
                'quarter must match pattern <year>Q<quarter_number> (ex.:2020Q3)'
            )
        return value
