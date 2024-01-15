import json
import pprint

selected_position = "B6"


def return_all_frets() -> list:
    """All the notes on the fretboard"""

    with open("data/notes_on_fretboard.json", "r") as file:
        all_notes = json.load(file)

    return all_notes


def return_indexes_for_all_keys() -> list[object]:
    """All the note index number in a key by position:
    [
    { "B6": [4, 6, 7, 16, 18, 19, 28, 30, 32, 40, 42, 52, 53, 55, 64, 66, 67] },
    { "E3": [4, 5, 7, 16, 18, 19, 28, 30, 31, 40, 42, 52, 53, 55, 64, 65, 67] },
    ...
    ]
    """

    with open("data/keys_by_position.json", "r") as file:
        key_notes = json.load(file)

    return key_notes


def get_note_indexes_for_position(position: str) -> list:
    all_positions = return_indexes_for_all_keys()
    for key_position in all_positions:
        if position in key_position.keys():
            return key_position[position]


def return_all_frets_with_key(key_position: str) -> list[object]:
    """All the frets in fretboard with a new field for "pluck" if the note is in the key_position passed:

    [
    ...
    {'fret': 7,
     'image_file': None,
     'index': 67,
     'learn_status': None,
     'note': 'B',
     'pluck': True,
     'sound_file': None,
     'string': 'e'},
    ...

       ]

    """
    all_frets = return_all_frets()
    key_frets = get_note_indexes_for_position(key_position)

    for index in key_frets:
        for fret in all_frets:
            if fret["index"] == index:
                fret["pluck"] = True
    # for fret_number in key_frets:
    #     for fret_dict in all_frets:
    #         if fret_number == fret_dict["fret"]:
    #             fret_dict["pluck"] = True
    #         if fret_dict["note"] == key_position[0]:
    #             fret_dict["root"] = True
    #             # updated_frets.append(fret_dict)

    # return matching
    return all_frets


def fretboard_matrix(notes: list[object]):
    fret = 1
    fret_group = []
    fretboard = []

    while len(fretboard) < 12:
        for note in notes:
            if note["fret"] == fret:
                fret_group.append(note)
        fretboard.append(fret_group)
        fret_group = []
        fret += 1

    return fretboard
