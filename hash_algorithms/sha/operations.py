def rotate_right(number: int, shift: int, word_size: int) -> int:
    return (number >> shift) | (number << (word_size - shift))


def choose(x: int, y: int, z: int) -> int:
    return (x & y) ^ (~x & z)


def majority(x: int, y: int, z: int) -> int:
    return (x & y) ^ (x & z) ^ (y & z)
