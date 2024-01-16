def get_key(key_position):
    """Takes key position such as Gb1 or B6, and returns only the key letter, "G" if natural, Gb if accidental."""
    key = ""

    if len(key_position) == 2:
        key = key_position[0]
    elif len(key_position) == 3:
        key = key_position[:2]

    return key
