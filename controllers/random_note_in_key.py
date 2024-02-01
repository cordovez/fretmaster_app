import json
import random

from collections import namedtuple


def return_random_note_index_in_key(key_position):
    with open("data/keys_by_position.json", "r") as file:
        all_keys = json.load(file)

    for notes in all_keys:
        if key_position in notes.keys():
            notes_in_position = notes[key_position]

    return random.choice(notes_in_position)


def return_random_note_value(note_index: int) -> str:
    with open("data/notes_on_fretboard.json", "r") as file:
        all_frets = json.load(file)

        for fret in all_frets:
            if fret["index"] == note_index:
                return fret["note"]


RandomNote = namedtuple("RandomNote", ["note_index", "note_value"])


def get_random_note(key_position: str) -> RandomNote:
    note_index = return_random_note_index_in_key(key_position)
    note_value = return_random_note_value(note_index)

    return RandomNote(note_index, note_value)
