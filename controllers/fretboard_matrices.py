from collections import namedtuple

from helpers.frets import return_all_frets
from helpers.key_positions import select_key_position, select_random_key_position
from helpers.construct_fretboards import (
    combine_fretboard_with_key_notes,
    arrange_fretboard_as_matrix,
)


Fretboard = namedtuple("Fretboard", ["fretboard", "key_position"])


def fretboard_with_random_position() -> Fretboard:
    """Main Function combines helper functions to return a named tuple "Fretboard" with field names "fretboard" and "key_position"."""
    list_of_frets = return_all_frets()
    random_position_number, random_sequence = select_random_key_position()
    list_of_frets_with_plucked_notes = combine_fretboard_with_key_notes(
        list_of_frets, random_sequence
    )
    fretboard_matrix = arrange_fretboard_as_matrix(list_of_frets_with_plucked_notes)

    return Fretboard(fretboard_matrix, random_position_number)


def fretboard_with_specified_key(key_position) -> Fretboard:
    """Main Function combines helper functions to return a named tuple "Fretboard" with field names "fretboard" and "key_position". It takes a key_position string from an Enum class, such as 'B6'"""
    list_of_frets = return_all_frets()
    key_position, key_sequence = select_key_position(key_position)
    list_of_frets_with_plucked_notes = combine_fretboard_with_key_notes(
        list_of_frets, key_sequence
    )
    fretboard_matrix = arrange_fretboard_as_matrix(list_of_frets_with_plucked_notes)

    return Fretboard(fretboard_matrix, key_position)
