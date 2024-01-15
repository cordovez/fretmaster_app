# import pprint

# # from .note_indexes_in_key import return_notes_in_position
# from fretboards import return_fretboard_with_key_position


# def return_random_note_in_position(position: str) -> list:
#     """Function takes one position-shape as a parameter from available:
#     "B6", "E3", "A7", "D4", "G1", "C5", "F2", "Bb6", "Eb3", "Ab7", "Db4", "Gb1"; and uses it to construct a fretboard with True values where notes in the position fall
#     """

#     key_position = return_notes_in_position(position)
#     fretboard = return_notes_matrix()
#     return key_position_shape(key_position, fretboard)


# def return_notes_matrix() -> list:
#     """returns a matrix representing the frets on a guitar. If looking at a fretboard, the numbers first go down a string, before moving to next string. This is used to construct a virtual fretboard"""

#     notes_matrix = []

#     row = 1

#     while len(notes_matrix) < 12:
#         fret = list(range(row, row + 60 + 1, 12))
#         notes_matrix.append(fret)
#         row += 1

#     return notes_matrix


# def key_position_shape(key_position: str, fretboard: list) -> list:
#     """function uses the key_position and fretboard, to construct a new fretboard with the notes in the position"""

#     modified_matrix = []
#     for fret in fretboard:
#         modified_fret = []
#         for note in fret:
#             if note in key_position:
#                 modified_fret.append(True)
#             else:
#                 modified_fret.append(False)
#         modified_matrix.append(modified_fret)
#     return modified_matrix


# # pprint.pprint(return_random_note_in_position("B6"))


# # def fretboard_matrix(fretboard: list[object]) -> list:
# #     return [set(fret["fret"]) for fret in fretboard]


# # pprint.pprint(fretboard_matrix(return_fretboard_with_key_position("B6")))
