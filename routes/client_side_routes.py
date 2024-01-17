from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# from controllers.note_indexes_in_key import return_note_indexes
# from controllers.random_note_in_key import return_random_note_in_key
# from controllers.create_note_matrices import return_random_note_in_position
from models.key_position_enum import KeyPosition

from controllers.fretboards import return_all_frets_with_key
from controllers.fretboards import fretboard_matrix
from controllers.random_note_in_key import return_random_note_in_key
from controllers.extract_key_string import get_key

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
async def flashcards(request: Request, key_position: KeyPosition):
    notes = return_all_frets_with_key(key_position.value)
    fretboard = fretboard_matrix(notes)
    random_note = return_random_note_in_key(key_position.value)
    key = get_key(key_position.value)

    return templates.TemplateResponse(
        "flashcards.html",
        {
            "request": request,
            "fretboard": fretboard,
            "notes": notes,
            "random": random_note,
            "key": key,
        },
    )
