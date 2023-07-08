from datetime import datetime
import uvicorn
from fastapi import FastAPI, UploadFile
from sqlalchemy.orm import Session


app = FastAPI()

@app.post("/product/file")
async def create_upload_file(file: UploadFile):
    file_content = file.file.read().decode('UTF-8')
    products = []
    for item in file_content.split('\n'):
        if(len(item) > 0):
            products.append({
                "type": int(item[0]),
                "date": datetime.strptime(item[1:26], "%Y-%m-%dT%H:%M:%S%z"),
                "product": item[26:56],
                "value": float(item[56:66]),
                "seller": item[66: 86]
            })
    
    return products

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)