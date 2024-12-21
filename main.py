from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove
from fastapi.responses import Response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://lostpaws.netlify.app/"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.post("/remove-bg")
# async def remove_background(file: UploadFile):
#     input_image = await file.read()
#     output_image = remove(input_image)
#     return Response(output_image, media_type="image/png")

@app.get("/")
async def root():
    return {"message": "I'm alive"}

@app.get("/hello")
async def root():
    return {"message": "hello"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
