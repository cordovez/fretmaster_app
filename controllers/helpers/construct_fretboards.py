def combine_fretboard_with_key_notes(
    fretboard: list[dict], sequence: list
) -> list[dict]:
    # sourcery skip: use-itertools-product
    """A helper function to designate which frets are fretted. This is indicated by a new field ("pluck" : True ) for notes in the sequence passed in."""
    for note_index in sequence:
        for fret in fretboard:
            if fret["index"] == note_index:
                fret["pluck"] = True
    return fretboard


def arrange_fretboard_as_matrix(notes: list[dict]) -> list[list]:
    """A helper function that helps organise all the notes into a matrix which can then be used as a table data in HTML."""
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
    print(notes)
    return fretboard
