from datetime import datetime
from fastapi import APIRouter, HTTPException, UploadFile, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from products import create_product, create_products_from_list, get_products_list

product_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@product_router.post("/product/file", tags=["products"])
async def create_upload_file(file: UploadFile, db: Session = Depends(get_db)):
    file_content = file.file.read().decode('UTF-8')
    products = []
    for item in file_content.split('\n'):
        if(len(item) > 0):
            # try:
            products.append(create_product(db, {
                "type": int(item[0]),
                "date": datetime.strptime(item[1:26], "%Y-%m-%dT%H:%M:%S%z"),
                "product": item[26:56].strip(),
                "value": float(item[56:66]),
                "seller": item[66: 86].strip()
            }))
            # except Exception:
            #     raise HTTPException(status_code=400, detail="Worng file contents")
    # create_products_from_list(db, products)
    return products

@product_router.get("/product/list", tags=["products"])
async def get_product_list(db: Session = Depends(get_db)):
    return get_products_list(db=db)