import json

selected_position = "B6"


def return_positions() -> list:
    with open("data/notes_on_fretboard.json", "r") as file:
        all_notes = json.load(file)

    return all_notes


all_positions = return_positions()

for position in all_positions:
    if selected_position in position:
        print(position[selected_position])
