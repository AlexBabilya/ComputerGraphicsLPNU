from fastapi import Request, APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .rotation import animate_rotation

figure_motion_router = APIRouter()

templates = Jinja2Templates(directory="./templates")


@figure_motion_router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('figure_motion/index.html',
                                      {"request": request})


@figure_motion_router.get("/help", response_class=HTMLResponse)
async def help_info(request: Request):
    return templates.TemplateResponse('figure_motion/help.html',
                                      {"request": request})


@figure_motion_router.post("/rotate", response_class=HTMLResponse)
async def rotate(request: Request,
                 ax: int = Form(...),
                 bx: int = Form(...),
                 cx: int = Form(...),
                 ay: int = Form(...),
                 by: int = Form(...),
                 cy: int = Form(...),
                 decrease_factor: int = Form(...),
                 option: str = Form(...),):
    animate_rotation([[ax, ay], [bx, by], [cx, cy]], int(option),
                     decrease_factor)
    return templates.TemplateResponse('figure_motion/index.html',
                                      {"request": request})
