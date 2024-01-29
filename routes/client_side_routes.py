from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

from models.key_position_enum import KeyPosition

from controllers.fretboards import (
    return_all_frets_with_key,
)
from controllers.fretboards import fretboard_matrix
from controllers.random_note_in_key import return_random_note_in_key
from controllers.extract_key_string import get_key
from controllers.random_key import return_random_key

from dependencies.main_nav import get_nav
from dependencies.music_keys import get_music_keys

front_router = APIRouter()

templates = Jinja2Templates(directory="templates")


@front_router.get("/", response_class=HTMLResponse)
async def base(request: Request, nav_items: dict[str, str] = Depends(get_nav)):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "nav_items": nav_items,
        },
    )


@front_router.get("/shapes", response_class=HTMLResponse)
async def shapes(
    request: Request,
    nav_items: dict[str, str] = Depends(get_nav),
    keys: dict[str, str] = Depends(get_music_keys),
):
    # fretboard = fretboard_matrix(notes)
    return templates.TemplateResponse(
        "shapes.html",
        {
            "request": request,
            # "fretboard": fretboard,
        },
    )


@front_router.get("/keys", response_class=HTMLResponse)
async def keys(
    request: Request,
    nav_items: dict[str, str] = Depends(get_nav),
    keys: dict[str, str] = Depends(get_music_keys),
):
    return templates.TemplateResponse(
        "keys.html",
        {"request": request, "keys": keys, "nav_items": nav_items},
    )


@front_router.get("/triads", response_class=HTMLResponse)
async def triads(
    request: Request,
    nav_items: dict[str, str] = Depends(get_nav),
    keys: dict[str, str] = Depends(get_music_keys),
):
    return templates.TemplateResponse(
        "triads.html",
        {"request": request, "keys": keys, "nav_items": nav_items},
    )


@front_router.get("/keys/{key_position}", response_class=HTMLResponse)
async def random_note(
    request: Request,
    key_position: KeyPosition,
    nav_items: dict[str, str] = Depends(get_nav),
    keys: dict[str, str] = Depends(get_music_keys),
):
    notes = return_all_frets_with_key(key_position.value)
    fretboard = fretboard_matrix(notes)
    random_note = return_random_note_in_key(key_position.value)
    key = get_key(key_position.value)
    key_position = key_position.name

    return templates.TemplateResponse(
        "partials/random_note_key_shape.html",
        {
            "request": request,
            "fretboard": fretboard,
            "notes": notes,
            "random": random_note,
            "key": key,
            "key_position": key_position,
            "nav_items": nav_items,
            "keys": keys,
        },
    )


# @front_router.get("/keys/{key_position}", response_class=HTMLResponse)
# async def random_note(
#     request: Request,
#     key_position: KeyPosition,
#     nav_items: dict[str, str] = Depends(get_nav),
# ):
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
#             "nav_items": nav_items,
#         },
#     )


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
