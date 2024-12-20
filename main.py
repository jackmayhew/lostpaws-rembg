from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "I'm alive"}

@app.post("/remove-bg")
async def remove_background(file: UploadFile):
    input_image = await file.read()
    # Just return the image without processing for now
    return Response(input_image, media_type="image/png")