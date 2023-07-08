from datetime import datetime
from pydantic import BaseModel


class ProductBase(BaseModel):
    type: int
    description: datetime
    product: str
    value: float
    seller: str

    class Config:
        orm_mode = True