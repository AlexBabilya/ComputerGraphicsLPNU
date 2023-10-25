import webcolors
from fastapi import Request, APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .mandelbrot import Mandelbrot
from .brownian_motion import BrownianMotion

fractal_router = APIRouter()

templates = Jinja2Templates(directory="./templates")


@fractal_router.get("/", response_class=HTMLResponse)
async def fractals(request: Request):
    return templates.TemplateResponse('fractals/index.html',
                                      {"request": request})


@fractal_router.get("/help", response_class=HTMLResponse)
async def help_fractals(request: Request):
    return templates.TemplateResponse('fractals/help.html',
                                      {"request": request})


@fractal_router.post("/show_fractal", response_class=HTMLResponse)
async def show_fractal(request: Request,
                       max_iter: int = Form(...),
                       color: str = Form(...),
                       dt: int = Form(...),
                       diffusion_coefficient: int = Form(...),
                       type: str = Form(...),
                       width: int = Form(...),
                       height: int = Form(...)):

    fractal = Mandelbrot(max_iter,
                         width, height,
                         webcolors.hex_to_rgb(color))

    if type == 'brownian_motion':
        fractal = BrownianMotion(max_iter,
                                 color,
                                 dt,
                                 diffusion_coefficient)

    fractal.show_graph()

    return templates.TemplateResponse('fractals/partials/add_form.html',
                                      {"request": request})
