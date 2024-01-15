import json


def return_notes_in_position(key_position):
    with open("data/notes_by_index.json", "r") as file:
        all_notes = json.load(file)

    for position in all_notes:
        if key_position in position and position[key_position]:
            notes_in_position = position[f"{key_position}"]
    return notes_in_position
