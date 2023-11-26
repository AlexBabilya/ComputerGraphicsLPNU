from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from modules.fractals.routers import fractal_router
from modules.color_schemas.routers import color_schemas_router
from modules.figure_motion.routers import figure_motion_router


app = FastAPI()

templates = Jinja2Templates(directory="./templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root_page(request: Request):
    return templates.TemplateResponse('home/index.html', {"request": request})

app.include_router(fractal_router, prefix="/fractals")
app.include_router(color_schemas_router, prefix="/color_schemas")
app.include_router(figure_motion_router, prefix="/figure_motion")
