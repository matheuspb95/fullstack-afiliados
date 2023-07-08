from typing import Union
from sqlalchemy import Float, Column, DateTime, Integer, String

from pydantic import BaseModel


class ProductBase(BaseModel):
    type: int
    description: DateTime
    product: str
    value: float
    seller: str

    class Config:
        orm_mode = True