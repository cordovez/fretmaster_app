from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

front_router = APIRouter()

templates = Jinja2Templates(directory="templates")


@front_router.get("/circle", response_class=HTMLResponse)
async def circle_of_fourths(
    request: Request,
):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Circle of Fourths"}
    )
