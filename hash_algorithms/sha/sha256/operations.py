from hash_algorithms.sha.operations import rotate_right


def rot_r(number: int, shift: int) -> int:
    return rotate_right(number, shift, 32)


def big_sigma0(x: int) -> int:
    return rot_r(x, 2) ^ rot_r(x, 13) ^ rot_r(x, 22)


def big_sigma1(x: int) -> int:
    return rot_r(x, 6) ^ rot_r(x, 11) ^ rot_r(x, 25)


def sigma0(x: int) -> int:
    return rot_r(x, 7) ^ rot_r(x, 18) ^ (x >> 3)


def sigma1(x: int) -> int:
    return rot_r(x, 17) ^ rot_r(x, 19) ^ (x >> 10)
