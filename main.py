import os
os.environ['U2NET_HOME'] = '/opt/models/'

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from rembg import remove
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "I'm alive"}

@app.post("/remove-bg")
async def remove_background(file: UploadFile):
    logger.info("Got image upload request")
    try:
        input_image = await file.read()
        logger.info("Read image file")
        output_image = remove(input_image)
        logger.info("Successfully removed background")
        return Response(output_image, media_type="image/png")
    except Exception as e:
        logger.error(f"Error in remove_background: {str(e)}")
        raise