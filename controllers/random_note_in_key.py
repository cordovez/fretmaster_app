import json
import random


def return_random_note_in_key(key_position):
    with open("data/keys_by_position.json", "r") as file:
        all_keys = json.load(file)

    for notes in all_keys:
        if key_position in notes.keys():
            notes_in_position = notes[key_position]

    # for position in all_notes:
    #     if key_position in position and position[key_position]:
    #         notes_in_position = position[f"{key_position}"]

    return random.choice(notes_in_position)


# [4, 6, 7, 16, 18, 19, 28, 30, 32, 40, 42, 52, 53, 55, 64, 66, 67]
print(return_random_note_in_key("B6"))
