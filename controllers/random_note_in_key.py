import json
import random


def return_random_note_in_key(key_position):
    with open("data/keys_by_position.json", "r") as file:
        all_keys = json.load(file)

    for notes in all_keys:
        if key_position in notes.keys():
            notes_in_position = notes[key_position]

    return random.choice(notes_in_position)
