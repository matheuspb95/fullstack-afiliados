from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session

from .models import Product
from .schemas import ProductBase

def create_product(db: Session, product: ProductBase):
    db_product = Product(
        type=product["type"], 
        date=product["date"], 
        product=product["product"], 
        value=product["value"], 
        seller=product["seller"]
    )
    try:
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
    except Exception:
        raise HTTPException(status_code=500, detail="Error on database, try again later")
    print(db_product.to_dict())
    return db_product.to_dict()

def create_products_from_list(db: Session, products: List[ProductBase]):
    db_products = [Product(
        type=product["type"], 
        date=product["date"], 
        product=product["product"], 
        value=product["value"], 
        seller=product["seller"]
    ) for product in products]
    try:
        db.add_all(db_products)
        db.commit()
        db.refresh(db_products)
    except Exception:
        raise HTTPException(status_code=500, detail="Error on database, try again later")
    return db_products

def get_products_list(db: Session, skip=0, limit=100):
    return db.query(Product).offset(skip).limit(limit).all()