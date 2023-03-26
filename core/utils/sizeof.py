from math import ceil


def sizeof_int(number: int) -> int:
    return ceil(number.bit_length() / 8.0)
