from typing import List


def message_preprocess(message: bytes) -> List[bytes]:
    padding_message = _add_padding_to_message(message)

    blocks = []
    for block_index in range(0, len(padding_message), 64):
        blocks.append(padding_message[block_index : block_index + 64])

    return blocks


def _add_padding_to_message(message: bytes) -> bytes:
    message_length = len(message)

    padding_message = message + bytes([0b10000000])

    while (len(padding_message) + 8) % 64 != 0:
        padding_message += bytes([0b00000000])

    padding_message += message_length.to_bytes(8, "big")

    return padding_message


