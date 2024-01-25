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


# @front_router.get("/flashcards/positions", response_class=HTMLResponse)
# async def positions(request: Request, key_position: KeyPosition):
#     notes = return_all_frets_with_key(key_position.value)
#     fretboard = fretboard_matrix(notes)
#     random_note = return_random_note_in_key(key_position.value)
#     key = get_key(key_position.value)
#     key_position = key_position.name

#     return templates.TemplateResponse(
#         "flashcards_random_note.html",
#         {
#             "request": request,
#             "fretboard": fretboard,
#             "notes": notes,
#             "random": random_note,
#             "key": key,
#             "key_position": key_position,
#         },
#     )


@front_router.get("/flashcards/positions", response_class=HTMLResponse)
async def positions(
    request: Request,
):
    return templates.TemplateResponse(
        "positions.html",
        {
            "request": request,
        },
    )


@front_router.get("/flashcards/{key_position}", response_class=HTMLResponse)
async def random_note(request: Request, key_position: KeyPosition):
    notes = return_all_frets_with_key(key_position.value)
    fretboard = fretboard_matrix(notes)
    random_note = return_random_note_in_key(key_position.value)
    key = get_key(key_position.value)
    key_position = key_position.name

    return templates.TemplateResponse(
        "flashcards_random_note.html",
        {
            "request": request,
            "fretboard": fretboard,
            "notes": notes,
            "random": random_note,
            "key": key,
            "key_position": key_position,
        },
    )


@front_router.get("/flashcards/{key_position}/notes", response_class=HTMLResponse)
async def update_note_set(request: Request, key_position: KeyPosition):
    notes = return_all_frets_with_key(key_position.value)
    fretboard = fretboard_matrix(notes)
    random_note = return_random_note_in_key(key_position.value)
    key = get_key(key_position.value)
    key_position = key_position.name

    return templates.TemplateResponse(
        "note_set.html",
        {
            "request": request,
            "notes": notes,
            "fretboard": fretboard,
            "random": random_note,
            "key": key,
            "key_position": key_position,
        },
    )


@front_router.get(
    "/flashcards/{key_position}/notes/answer", response_class=HTMLResponse
)
async def display_random_note(request: Request, key_position: KeyPosition):
    notes = return_all_frets_with_key(key_position.value)
    fretboard = fretboard_matrix(notes)
    random_note = return_random_note_in_key(key_position.value)
    key = get_key(key_position.value)
    key_position = key_position.name

    return templates.TemplateResponse(
        "partials/random_note_answer.html",
        {
            "request": request,
            "notes": notes,
            "fretboard": fretboard,
            "random": random_note,
            "key": key,
            "key_position": key_position,
        },
    )
