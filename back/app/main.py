import uvicorn
from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.post("/product/file")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)