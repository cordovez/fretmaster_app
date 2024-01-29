import json
import random

from collections import namedtuple

Position = namedtuple("Position", ["position", "sequence"])


def return_random_key() -> Position:
    with open("data/position_shapes.json", "r") as file:
        all_positions = json.load(file)

        rand_num = random.randint(0, 6)
        sequence = list(all_positions[rand_num].values())[0]
        return Position(rand_num + 1, sequence)


# print(return_note_sequence_for_random_position())
