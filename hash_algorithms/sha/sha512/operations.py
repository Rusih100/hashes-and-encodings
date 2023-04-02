from hash_algorithms.sha.operations import rotate_right


def rot_r(number: int, shift: int) -> int:
    return rotate_right(number, shift, 64)


def big_sigma0(x: int) -> int:
    return rot_r(x, 28) ^ rot_r(x, 34) ^ rot_r(x, 39)


def big_sigma1(x: int) -> int:
    return rot_r(x, 14) ^ rot_r(x, 18) ^ rot_r(x, 41)


def sigma0(x: int) -> int:
    return rot_r(x, 1) ^ rot_r(x, 8) ^ (x >> 7)


def sigma1(x: int) -> int:
    return rot_r(x, 19) ^ rot_r(x, 61) ^ (x >> 6)
