from pydantic import BaseModel, validator
from datetime import date
from typing import Optional, Union, List
from enum import Enum


class Type(str, Enum):
    cumulative = 'cumulative'
    usual = 'usual'


class Grouping(str, Enum):
    weekly = 'weekly'
    bi_weekly = 'bi-weekly'
    monthly = 'monthly'


class TimelineQuery(BaseModel):
    start_date: date
    end_date: date
    type: Type
    grouping: Grouping
    stars: Optional[List[int]] = None
    brand: Optional[List[str]] = None
    asin: Optional[List[str]] = None
    source: Optional[List[str]] = None

    @validator('end_date')
    def check_date(cls, end_date, values, **kwargs):
        if end_date < values['start_date']:
            raise ValueError('Invalid date')
        return end_date

    class Config:
        use_enum_values = True
