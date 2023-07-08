import uvicorn
from fastapi import FastAPI, UploadFile
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/product/file")
async def create_upload_file(file: UploadFile):
    contents = file.file.read()
    return {"contents": contents}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)