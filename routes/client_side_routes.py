from fastapi import APIRouter, Request, Depends, Header
from fastapi.responses import HTMLResponse
from typing import Optional
from fastapi.templating import Jinja2Templates

from models.key_position_enum import KeyPosition


from controllers.random_note_in_key import get_random_note
from controllers.fretboard_matrices import (
    fretboard_with_random_position,
    fretboard_with_specified_key,
)
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
    hx_request: Optional[str] = Header(None),
    nav_items: dict[str, str] = Depends(get_nav),
    keys: dict[str, str] = Depends(get_music_keys),
):
    context = {
        "request": request,
        "nav_items": nav_items,
    }
    if hx_request:
        return templates.TemplateResponse("partials/basic_flashcard.html", context)

    return templates.TemplateResponse("shapes.html", context)


@front_router.get("/shapes/draw", response_class=HTMLResponse)
async def shapes_draw(
    request: Request,
    hx_request: Optional[str] = Header(None),
    nav_items: dict[str, str] = Depends(get_nav),
    # keys: dict[str, str] = Depends(get_music_keys),
):
    fretboard, position = fretboard_with_random_position()

    context = {
        "request": request,
        "nav_items": nav_items,
        "fretboard": fretboard,
        "position": position,
    }
    if hx_request:
        print(hx_request)
        return templates.TemplateResponse("partials/_shapes_flashcard.html", context)
    return templates.TemplateResponse(
        "partials/_shapes_flashcard.html",
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


@front_router.get("/keys/{key_position}", response_class=HTMLResponse)
async def random_note(
    request: Request,
    key_position: KeyPosition,
    nav_items: dict[str, str] = Depends(get_nav),
    keys: dict[str, str] = Depends(get_music_keys),
):
    fretboard, position = fretboard_with_specified_key(key_position.value)
    random_note_index, random_note_value = get_random_note(key_position.value)

    return templates.TemplateResponse(
        "partials/_keys_flashcard.html",
        {
            "request": request,
            "fretboard": fretboard,
            "position": position[-1],
            "random": random_note_index,
            "key_position": key_position.value,
            "nav_items": nav_items,
            "note_value": random_note_value,
        },
    )


@front_router.get("/roots", response_class=HTMLResponse)
async def triads(
    request: Request,
    nav_items: dict[str, str] = Depends(get_nav),
    keys: dict[str, str] = Depends(get_music_keys),
):
    return templates.TemplateResponse(
        "roots.html",
        {"request": request, "keys": keys, "nav_items": nav_items},
    )
