from typing import List

from hash_algorithms.sha.operations import rotate_right


def message_preprocess(message: bytes) -> List[bytes]:
    padding_message = _add_padding_to_message(message)

    blocks = []
    for block_index in range(0, len(padding_message), 64):
        blocks.append(padding_message[block_index : block_index + 64])

    return blocks


def _add_padding_to_message(message: bytes) -> bytes:
    message_length = len(message) * 8

    padding_message = message + bytes([0b10000000])

    while (len(padding_message) * 8 + 64) % 512 != 0:
        padding_message += bytes([0b00000000])

    padding_message += message_length.to_bytes(8, "big")

    return padding_message


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
