from fastapi import Request, APIRouter, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import io

from .green_saturation import change_green_saturation

color_schemas_router = APIRouter()

templates = Jinja2Templates(directory="./templates")


@color_schemas_router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('color_schemas/index.html',
                                      {"request": request})


@color_schemas_router.get("/help", response_class=HTMLResponse)
async def help_info(request: Request):
    return templates.TemplateResponse('color_schemas/help.html',
                                      {"request": request})


@color_schemas_router.post("/change/")
async def process_image(request: Request, coef: str = Form(...),
                        file: UploadFile = File(...)):
    contents = await file.read()
    image = io.BytesIO(contents)
    change_green_saturation(image, int(coef))
    return templates.TemplateResponse('color_schemas/partials/add_form.html',
                                      {"request": request})
