def rotate_right(number: int, shift: int, size: int) -> int:
    return (number >> shift) | (number << (size - shift))


def choose(x: int, y: int, z: int) -> int:
    return (x & y) ^ (~x & z)


def majority(x: int, y: int, z: int) -> int:
    return (x & y) ^ (x & z) ^ (y & z)
