from sqlalchemy import Float, Column, DateTime, Integer, String

from database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Integer)
    date = Column(DateTime)
    product = Column(String)
    value = Column(Float)
    seller = Column(String)

