from fastapi import FastAPI, File, UploadFile
from rembg import remove
from fastapi.responses import Response

app = FastAPI()

@app.get("/")  # Add a root endpoint
async def root():
    return {"status": "ok"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/remove-bg")
async def remove_background(file: UploadFile):
    input_image = await file.read()
    output_image = remove(input_image)
    return Response(output_image, media_type="image/png")