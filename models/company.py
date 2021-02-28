from typing import Any, Dict, List

from pydantic import BaseModel, Field, condecimal
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


class FinancialStatement(BaseModel):
    title: str = Field(...)
    quarter: str = Field(...)  # ex.: 2020Q3
    value: condecimal(decimal_places=2)  # type: ignore
