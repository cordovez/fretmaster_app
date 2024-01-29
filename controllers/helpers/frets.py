import json


def return_all_frets() -> list[dict]:
    """A helper function to help construct a fretboard. It returns a list of all note objects.

    [
    {
      "string": "E",
      "fret": 1,
      "index": 1,
      "note": "F",
      "learn_status": null,
      "image_file": null,
      "sound_file": null
    }, ...
    ]

    """

    with open("data/notes_on_fretboard.json", "r") as file:
        all_notes = json.load(file)

    return all_notes
