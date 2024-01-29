import random
from collections import namedtuple
import json


Position = namedtuple("Position", ["position", "sequence"])


def select_random_key_position() -> Position:
    """A helper function that selects a random position and the related sequence of note indexes as a list.

    It returns a named tuple "Position" with field names "position" and "sequence"

    """
    random_number = random.randint(0, 6)
    random_sequence_number = str(random_number + 1)

    with open("data/position_sequences.json") as file:
        sequences = json.load(file)

        for sequence in sequences:
            if random_sequence_number in sequence:
                return Position(
                    random_sequence_number, sequence[random_sequence_number]
                )


def select_key_position(key_position: str) -> Position:
    """A helper function that selects a random position and the related sequence of note indexes as a list.

    It returns a named tuple "Position" with field names "position" and "sequence"

    """

    with open("data/keys_by_position.json") as file:
        sequences = json.load(file)

        for sequence in sequences:
            if key_position in sequence:
                return Position(key_position, sequence[key_position])
