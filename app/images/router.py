import shutil

from fastapi import APIRouter, UploadFile

from app.tasks.tasks import process_pic


router = APIRouter(
    prefix="/images",
    tags=["Загрузка картинок"]
)

@router.post("/hotels")
async def add_hotel_image(name: int, file: UploadFile):
    im_path = f"app/static/images/{name}.webp"
    with open(im_path, "wb+") as file_object:
        # We save the file to local storage (in practice, it is usually saved to remote storage)
        shutil.copyfileobj(file.file, file_object)
    # Give Celery a background task to process the image
    process_pic.delay(im_path)