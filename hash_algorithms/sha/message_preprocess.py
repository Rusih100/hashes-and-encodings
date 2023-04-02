from typing import List


def message_preprocess(message: bytes, block_size: int) -> List[bytes]:
    block_size_of_bytes = block_size // 8

    padding_message = _add_padding_to_message(message, block_size=block_size)

    blocks: List[bytes] = []
    for block_index in range(0, len(padding_message), block_size_of_bytes):
        blocks.append(
            padding_message[block_index : block_index + block_size_of_bytes]
        )

    return blocks


def _add_padding_to_message(message: bytes, block_size: int) -> bytes:
    block_size_of_bytes = block_size // 8
    message_length = len(message) * 8

    padding_message = message + bytes([0b10000000])

    while (len(padding_message) * 8 + block_size_of_bytes) % (
        block_size_of_bytes * 8
    ) != 0:
        padding_message += bytes([0b00000000])

    if block_size == 512:
        padding_message += message_length.to_bytes(8, "big")
    else:
        padding_message += message_length.to_bytes(16, "big")

    return padding_message
