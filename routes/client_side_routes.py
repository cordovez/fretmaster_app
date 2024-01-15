from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# from controllers.note_indexes_in_key import return_note_indexes
# from controllers.random_note_in_key import return_random_note_in_key
from controllers.create_note_matrices import return_random_note_in_position

front_router = APIRouter()

templates = Jinja2Templates(directory="templates")


@front_router.get("/", response_class=HTMLResponse)
async def base(
    request: Request,
):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
        },
    )


@front_router.get("/flashcards", response_class=HTMLResponse)
async def flashcards(
    request: Request,
):
    # notes = return_note_indexes("B6")
    # random_note = return_random_note_in_key("B6")
    fretboard = return_random_note_in_position("B6")

    return templates.TemplateResponse(
        "flashcards.html",
        {"request": request, "fretboard": fretboard},
        # {"request": request, "notes": notes, "random_note": random_note, "card": card},
    )
